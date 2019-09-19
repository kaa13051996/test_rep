from requests import get, codes
from re import search, MULTILINE
from os.path import isfile
from bs4 import BeautifulSoup
from pickle import load, dump

from const import URL, NAME_FILE_HASH, NAME_PICKLE_FILE, STUDENT
from bs_iter import BeautifulSoupIterator
from StudentsInfo import StudentInfo, get_rating_list, get_ranked, print_table
from Hash_info import HashInfo


def get_page(url=URL):
    data = get(url)
    if data.status_code != codes.OK:
        raise Exception(fr'Error page: URL {url}\n The status of calling page: {data.status_code}')
    return data.text


def get_table(data, file_hash=NAME_FILE_HASH, file_pickle=NAME_PICKLE_FILE):
    table = search(r'<tbody>[\s\S]+?</tbody>', data, MULTILINE)[0]
    with HashInfo(table.encode(), file_hash) as obj:
        data = load_data(table, name_file=file_pickle) if obj.current_hash == obj.last_hash \
            else update_data(table, name_file=file_pickle)
    print_table(data)
    return data


def load_data(table, name_file):
    print('Load results...')
    if isfile(name_file):
        with open(name_file, 'rb') as f:
            data = load(f)
    else:
        print('Pickle file do not exist!')
        data = update_data(table, name_file)
    return data


def update_data(table, name_file):
    print('Update results...')
    data = get_parse_data(table)
    with open(name_file, 'wb') as f:
        dump(data, f)
    return data


def get_parse_data(data):
    students_info = []
    soup = BeautifulSoup(data, 'lxml').tbody.contents
    for student in BeautifulSoupIterator(soup):
        students_info.append(StudentInfo(*[attr.text.strip() for attr in BeautifulSoupIterator(student)]))
    return get_rating_list(students_info, output=False)


if __name__ == '__main__':
    table = get_table(get_page())
    ranks = get_ranked(table, STUDENT)
