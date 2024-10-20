class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello, I am {self.name}, and I am {self.age} years old.")
    def get_older(self):
        self.age += 1
        print(f"I am now {self.age} years old.")

# Tests
p1 = Person("Tyler", 19)
p1.introduce()
p1.get_older()
    