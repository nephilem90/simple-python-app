import sqlite3
from dotenv import load_dotenv
import os


class SqLitePDO:
    def __init__(self, database):
        self.database = database
        self.results = []

    def insert(self, table_name, values):
        # create strings of comma separated values (value1,value2,value3)
        param = ','.join(f"'{value}'" for value in values.values())
        keys = ','.join(values)
        query = f"INSERT INTO {table_name} ({keys})  VALUES ({param})"
        self.exec_query(query)

    def select(self, table_name, where=None):
        query = "SELECT * FROM " + table_name
        if where is not None:
            query = query + " WHERE " + where
        return self.exec_query(query)

    def exec_query(self, query):
        connect = sqlite3.connect(self.database)
        connect.row_factory = sqlite3.Row
        cursor = connect.cursor()
        cursor.execute(query)
        fetch = cursor.fetchall()
        results = []
        for row in fetch:
            result = {}
            for key in row.keys():
                result[key] = row[key]
            results.append(result)
        self.results = results
        connect.commit()
        connect.close()
        return self

    def pop_results(self):
        results = self.results.copy()
        self.results = []
        return results

    @staticmethod
    def get_pdo():
        load_dotenv()

        db_path = os.getenv("DB_PATH")
        db_name = os.getenv("DB_NAME")
        db_location = f'{db_path}/{db_name}'
        if not os.path.isfile(db_location):
            print('ERRORE: database non trovato!')
            return
        return SqLitePDO(db_location)
