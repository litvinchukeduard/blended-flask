class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return self.__value
    
    def __repr__(self):
        return self.__value


class Email(Field):
    pass


class Name(Field):
    pass

class User:
    latest_id = 1

    def __init__(self, name:str, email:str):
        self.id = User.latest_id
        self.name = Name(name)
        self.email = Email(email)

        User.latest_id += 1