from dotenv import load_dotenv
import os
from SqLitePDO import SqLitePDO
import sys
import datetime
import time
import glob


class Migration:
    def __init__(self, pdo):
        self.pdo = pdo
        load_dotenv()
        self.migration_path = os.getenv('MIGRATION_PATH')
        self.migration_table = os.getenv('MIGRATION_TABLE')

    def create(self, file_name):
        now = time.time()
        now_string = datetime.datetime.fromtimestamp(now).strftime('%Y%m%d%H%M%S')
        sql_file_name = self.migration_path + '/' + now_string + '_' + file_name
        file = open(sql_file_name + ".sql", "w+")
        file.close()

    def migrate(self):
        sql_files = glob.glob(self.migration_path + '/*.sql')
        for sql_file in sql_files:
            if not self.pdo.select(self.migration_table, "script = '" + sql_file + "'").pop_results():
                file = open(sql_file, "r")
                self.pdo.exec_query(file.read())
                self.pdo.insert(self.migration_table, {'script': sql_file})

    def init(self):
        self.pdo.exec_query("CREATE TABLE `" + self.migration_table + "` (`script` TEXT NOT NULL PRIMARY KEY UNIQUE)")


migration = Migration(SqLitePDO.get_pdo())
if sys.argv[1] == 'init':
    migration.init()
if sys.argv[1] == 'create':
    migration.create(sys.argv[2])
if sys.argv[1] == 'migrate':
    migration.migrate()
