class Circle():
    pi = 3.1416

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def circumference(self):
        return 2 * self.pi * self.radius


mycircle = Circle(10)


# print(mycircle.radius)
# print(mycircle.area())
# print(mycircle.circumference())

class Animal():

    def __init__(self, fur):
        self.fur = fur

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating!')


# a = Animal()
# a.eat()
# a.report()

class Dog(Animal):

    def __init__(self, fur):
        Animal.__init__(self, fur)
        print('Dog created!')

    # Overwrite report method
    def report(self):
        print('I am a Dog!')


d = Dog('Fuzzy')
print(d.fur)
