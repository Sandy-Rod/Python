class User:
    def __init__(self, name, username):
        self._name = name
        self.__username = username

    @property
    def username(self):
        return self.__username
    
    def save(self, user_data):
        print(f"User {self} saved")


class StaffUser(User):
    def __init__(self, name, username, age, dni):
        super().__init__(name, username)
        self.__age = age
        self.__dni = dni

    def manage_accounts(self, accounts_list):
        print("updating stuffs in accounts")




staff_user2 = StaffUser(username="Pepe", name="Pepe", age=25, dni="12345678")
print(staff_user2._name)



#Herencia Múltiple

class StaffMixin:
    def manage_accounts(self, accounts_list):
        print("updating stuffs in accounts")


#creación de clase que hereda dos clases

class StaffUser2(StaffMixin, User):
    def __init__(self, name, username, age, dni):
        super().__init__(name, username)
        self.__age = age
        self.__dni = dni

