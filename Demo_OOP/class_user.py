class User:
    def __init__(self, userName, age):
        self.__UserName =userName
        self.__Age = age
    def GetUserName(self):
        return self.__UserName
    def GetAge(self):
        return self.__Age
    def GetUobj(self):
        return self.__Age, self.GetUserName()

def main():
    u1 = User("Ali", 20)
    print(u1.GetUserName())
    print(u1.GetAge())
    print(u1.GetUobj())

    u2 = User("Hasan", 25)
    print(u2.GetUserName())
    print(u2.GetAge())
    print(u2.GetUobj())

if __name__ == '__main__':main()