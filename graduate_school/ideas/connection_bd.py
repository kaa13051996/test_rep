import sqlite3

from const import BD_FILE


class SQLLiteConn:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except Exception as ex:
            raise Exception(ex.args[0])
        return self

    def update(self, data):
        cur = self.conn.cursor()
        self.conn.commit()

    def insert(self, data):
        self.cursor.executemany("""INSERT INTO students 
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data
                                )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


if __name__ == '__main__':
    db = BD_FILE
    students_info = []

    with SQLLiteConn(db) as conn:
        # cursor = conn.cursor()
        conn.cursor.execute("""CREATE TABLE students(
                          No int, Full_name text, 
                          SS int, English  int, Philosophy int, Individual_achievements int, Total_points int,
                          Enrollment_Category text, Document text, Status text)
                       """)
