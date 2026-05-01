
# 3-m
class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def eat(self):
        print(self.name)
        print(self.age)
        print(self.type)

class Dog(Animal):
    def __init__(self, name, age, type, brend, color):
        super().__init__(name, age, type)
        self.brend = brend
        self.color = color

    def eat(self):
        super().eat()
        print(self.brend)
        print(self.color)

a1 = Dog("Alex", 2, "dog", "dog", "qora")
a1.eat()
