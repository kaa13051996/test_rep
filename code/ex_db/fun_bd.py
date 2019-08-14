import sqlite3
from ex_db.struct_bd import StructBD, get_type_column, get_name_columns


class Connection:
    def __init__(self, name_bd='ex_sqlite.db'):
        self.conn = Connection.__create_conn(name_bd)
        self.cursor = self.conn.cursor()

    @staticmethod
    def __create_conn(name):
        try:
            return sqlite3.Connection(name)
        except Exception as ex:
            raise Exception(ex.args[0])

    def create_tb(self, name_tb, name_columns, type_columns):
        par_create_table = ''
        for nm, tp in zip(name_columns, type_columns):
            par_create_table = par_create_table + f'{nm} {tp}, '

        olo = par_create_table[:-2]
        self.cursor.execute(f'CREATE TABLE {name_tb} ({par_create_table[:-2]})')

    def insert(self, name_tb, rows):
        if rows is list:
            self.cursor.execute('INSERT INTO ? VALUES (? ? ? ? ?)', rows)
        else:
            self.cursor.execute('INSERT INTO ? VALUES (? ? ? ? ?)', (name_tb, rows.date, rows.trans, rows.symbol, rows.qty, rows.price))
        self.save()

    def select(self, name_tb):
        self.cursor.execute(
            f'SELECT * FROM {name_tb}')

    def save(self):
        self.conn.commit()

    # def bd_w(self):
    #     with open('dump.sql', 'w') as f:
    #         for line in self.conn.iterdump():
    #             f.write('%s\n' % line)

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    row = StructBD('2006-01-05', 'BUS', 'RHAT', 100, 35.14)
    conn = Connection()
    conn.create_tb(row.BD_NAME, get_name_columns(), get_type_column())
    conn.insert(row.BD_NAME, row)
    conn.select(row.BD_NAME)
    row2 = StructBD('2007-02-06', 'CAR', 'CAT', 198, 12.764)
    conn.insert(row2.BD_NAME, row2)
    conn.select(row2.BD_NAME)
    conn.__del__()
    print('Success!')
