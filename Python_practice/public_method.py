"""
Overriding is the property of a class to
change the implementation of a method provided by one of its base classes.

"""


class PublicMethod:
    def __init__(self):
        print('Public_Class_Constructor')
        self.public_variable = ''
        self.__private_variable = ''

    def public_method(self):
        print('public_method')
        self.public_variable = 'Public_method'
        self.__private_variable = 'Private_method'

    def __private_method(self):
        print('private_method')
