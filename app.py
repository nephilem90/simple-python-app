from UserModel import UserModel
from SqLitePDO import SqLitePDO
from UserWrite import UserWrite

pdo = SqLitePDO.get_pdo()

params = {
    'name': 'pippo',
    'email': 'test@email.com',
    'password': '1234'
}

user = UserModel.fromArray(params)
userWriter = UserWrite(pdo)
userWriter.insert(user)
