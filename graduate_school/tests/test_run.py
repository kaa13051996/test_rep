from pathlib import Path
from mock import patch

from main import get_table


def read_text(file_url):
    with open(file_url, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


# def test_run():
#     with patch('itertools.permutations') as perm_mock:
#         perm_mock.return_value = get_page
#     assert get_table(read_text(file_url), file_hash=file_hash, file_pickle=file_pickle) ==


if __name__ == '__main__':
    file_url = Path('resource/text')
    file_hash = 'test_hash'
    file_pickle = 'test_pickle'
    table = get_table(read_text(file_url), file_hash=file_hash, file_pickle=file_pickle)
