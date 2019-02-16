from UserModel import UserModel
from SqLitePDO import SqLitePDO
from UserWrite import UserWrite
from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
DB_NAME = os.getenv("DB_NAME")
DB_LOCATION = DB_PATH + '/' + DB_NAME
if not os.path.isfile(DB_LOCATION):
    print('ERRORE: database non trovato!')
    exit(-1)

pdo = SqLitePDO(DB_LOCATION)

params = {
    'name': 'pippo',
    'email': 'test@email.com',
    'password': '1234'
}

user = UserModel.fromArray(params)
userWriter = UserWrite(pdo)
userWriter.insert(user)
