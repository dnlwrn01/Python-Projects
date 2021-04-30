
#create class
class Protected:
    def __init__(self):
        self.__userName = 'marioCartHero' #define private var
        self._age = 25 #define public var
    def getPrivate(self):
        print(self.__userName)
    def setPrivate(self):
        self.__userName = private

#return private and protected values
obj = Protected()
obj.getPrivate()
print(obj._age)
