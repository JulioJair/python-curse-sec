# OOP Allows to creat their own objects that have methods and attributes.
# Objects are string, list, dicts, and other and have methods
# Those methods are called by the .method_name() syntax
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)


class Sample():
    pass


x = Sample()
print(type(x))


class Dog():
    # CLASS OBJECT ATTRIBUTES
    species = 'mammal'

    def __init__(self, input_breed, name):
        self.breed = input_breed
        self.name = name


sam = Dog('Lab', 'Frankie')
new_dog = Dog('Golden', 'Cindy')
print(sam.breed)
print(sam.name)
print(sam.species)
print(new_dog.species)
