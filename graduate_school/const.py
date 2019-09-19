from pathlib import Path

URL = r'https://postgraduate.tusur.ru/ru/aspirantura/kak-postupit/spiski/ochnaya/2019-09-06-01-informatika-i-vychislitelnaya-tehnika-fulltime?kind_list=all'
STUDENT = [{'full_name': 'Слезкин Артем Олегович', 'id': None}, {'full_name': 'Перминов Петр', 'id': 26}]

# PATHS
ROOT_DIR = Path(__file__).parent
NAME_FILE_HASH = ROOT_DIR / 'hash'
NAME_PICKLE_FILE = 'students_info'

# BD
BD_FILE = 'incoming_students.db'
TB_NAME = 'students'

# DEL
BD_NAME = 'sakila'
USER = 'alisa'
PASSWOED = '0pssfrbd-'
