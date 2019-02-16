from UserModel import UserModel
from SqLitePDO import SqLitePDO
from UserWrite import UserWrite

params = {
    'name': 'pippo',
    'email': 'test@email.com',
    'password': '1234'
}

user = UserModel.fromArray(params)
pdo = SqLitePDO('db/database.db')
write = UserWrite(pdo)
write.insert(user)
