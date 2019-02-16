class UserWrite:
    def __init__(self, pdo):
        self.tableName = 'users'
        self.pdo = pdo

    def insert(self, userModel):
        user = userModel.toArray()
        self.pdo.insert(self.tableName, userModel.toArray())

