from hashlib import md5
from os.path import isfile


class HashInfo:
    def __init__(self, table, name):
        self.current_hash = md5(table).hexdigest()
        self.last_hash = None
        self.file_name = name

    def __enter__(self):
        if not isfile(self.file_name):
            pass
        else:
            with open(self.file_name, encoding='utf-8') as f:
                self.last_hash = f.read()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.last_hash is None or self.current_hash != self.last_hash:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                f.write(self.current_hash)
        if exc_val:
            raise


if __name__ == '__main__':
    TABLE = ''.encode()
    NAME_HASH = 'hash'
    NAME_PICKLE = 'students_info'
    with HashInfo(TABLE, NAME_HASH) as obj:
        pass
