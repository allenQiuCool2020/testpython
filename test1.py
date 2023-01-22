class Pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("bark")

class Fish(Pet):
    pass


p = Pet("Tim", 9)
# p.show()
c = Cat("Tom", 10)
# c.show()
d = Dog("Carl", 10)


f = Fish("Memo", 8)
f.speak()

c.speak()
p.speak()
d.speak()