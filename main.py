class Person:
    def __init__(self):
        self.name = "Evgen"
        self.age = 20
        self.height = 180
        self.__weight = 70

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Weight: {self.__weight}")

    def __inform(self):
        pass


class Student(Person):
    def __init__(self):
        super().__init__()
        self.name = "Maks"
        self.progress = 10

    def info(self):
        super().info()
        print(f"Name: {self.name}, Progress: {self.height}")

class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.age = 35
    


s = Student()
t = Teacher()

s.info()
t.info()



class Grandparent:
    def info(self):
        print("i'm grandparent")

class Parent(Grandparent):
    def info(self):
        print("i'm parent")

class Child(Parent):
    def __init__(self):
        super().info()



