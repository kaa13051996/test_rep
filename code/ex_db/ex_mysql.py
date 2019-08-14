import mysql.connector


class MySQLConn:
    __DB_NAME = 'sakila'
    __ACCOUNTS = {'alisa': '0pssfrbd-', 'root': '0pssfrbd-'}

    def __init__(self, user='alisa'):
        self.user = user
        self.cnx = mysql.connector.connect(user=self.user, password=self.__ACCOUNTS[USER],
                                           host='127.0.0.1',
                                           database=self.__DB_NAME)
        self.cursor = self.cnx.cursor()
        self.cnx.close()

    # def __del__(self):
    #     self.cnx.close()


if __name__ == '__main__':
    USER = 'root'
    obj = MySQLConn(USER)



