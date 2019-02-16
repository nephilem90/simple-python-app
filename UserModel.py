class UserModel:
    name = ''
    email = ''
    password = ''

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        return self

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email
        return self

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
        return self

    @staticmethod
    def fromArray(params):
       user = UserModel()
       user.setEmail(params['email'])
       user.setName(params['name'])
       user.setPassword(params['password'])
       return user

    def toArray(self):
        return {
            'email': self.email,
            'name': self.name,
            'password': self.password
        }

