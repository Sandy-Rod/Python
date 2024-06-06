from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod

class AbstractUserRepository(ABC):

    def __init__(self, username):
        self.__username = username

    @abstractproperty
    def username(self):  #todo lo que herede de User tiene que tener este método
        pass
    
    @abstractmethod
    def save_self(self, user_data): #todo lo que herede de User tiene que tener este método
        pass
    
    @abstractclassmethod
    def save_cls(cls, user_data): #todo lo que herede de User tiene que tener este método
        raise NotImplementedError("Must be implemented by subclass")

class MySQLUserRepository(AbstractUserRepository):
    pass



class InMemoryUserRepository(AbstractUserRepository):
    def __init__(self, username):
        self.__username = username


    def username(self):
        return self.__username
    
    def save_self(self, user_data):
        print(f"User {self} saved")

    def save_cls(cls, user_data):
        print(f"User {cls} saved")


#user = MySQLUserRepository(username="paco") 
#print(user)

user = InMemoryUserRepository(username="paco")
user.save_self(user_data=[])
