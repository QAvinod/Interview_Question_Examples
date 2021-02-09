import override_class


class Sreevani:
    def __init__(self):
        print('sreevani_class')

    def sreevani_method(self):
        print('sreevani_method')
        sreevani_inherit = override_class.vinod('baby')
        sreevani_inherit.vinod_method()
        print(sreevani_inherit.vinod)


Object = Sreevani()
Object.sreevani_method()
