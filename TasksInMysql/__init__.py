import pymysql

class DatabaseContextManager():
    def __init__(self, is_select=False):
        self.is_select = is_select

    def __enter__(self):
        self.connection = pymysql.connect(host="127.0.0.1", user="root", password="root", database="university")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.is_select == False:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()
