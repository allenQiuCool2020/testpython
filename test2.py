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



c = Cat("Tom", 10)
d = Dog("Carl", 10)

c.speak()

d.speak()