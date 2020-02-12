#Method Overriding
class Dog():
    def sound(self):
        print("woow woow")

class Cat(Dog):
    def sound(self):
        print("Meeow Meow")

c = Cat()
c.sound()
d= Dog()
d.sound()
