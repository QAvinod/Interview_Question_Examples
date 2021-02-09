import public_method


class PublicMethod2(public_method.PublicMethod):
    def __init__(self):
        super(PublicMethod2, self).__init__()
        print('private_class_constructor')
        self.public_method()
        print(self.public_variable)


Object = PublicMethod2()
