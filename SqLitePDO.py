import sqlite3

class SqLitePDO:
    def __init__(self, database):
        self.database = database

    def insert(self, tableName, values):
        notForFirst = ""
        param = ""
        keys = ""
        for key, value in values.items():
            keys = keys + notForFirst + key
            param = param + notForFirst + "'" + value + "'"
            notForFirst = ","
        query = "INSERT INTO " + tableName + " (" + keys + ")" + " VALUES (" + param + ")"
        self.__excecQuery__(query)

    def __excecQuery__(self, query):
        connect = sqlite3.connect(self.database)
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        connect.close()


