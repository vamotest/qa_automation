import pymysql


class DataBase:

    def __init__(self, host, name, user, password, port):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.connection = pymysql.connect(
            host=host,
            database=name,
            user=user,
            password=password,
            port=port,
            autocommit=True)
        self.connection.autocommit(True)

    def destroy(self):
        self.connection.close()

    def add_currency(self):

        cursor = self.connection.cursor()
        try:
            cursor.execute(
                'INSERT INTO oc_currency (title, code, symbol_left, '
                'symbol_right, decimal_place, value, status, date_modified) '
                'VALUES ("Russia Ruble", "RUB", "1" , "₽", "1", "1", "1", '
                '"2020-01-01 00:00:00")')
        finally:
            cursor.close()

    def delete_currency(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                'DELETE FROM bitnami_opencart.oc_currency WHERE code="RUB"')
        finally:
            cursor.close()
