class Person:
    def __init__(self, name):
        self.name = name
        self.age = 20
        self.height = 180
        self.__weight = 70

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Weight: {self.__weight}")

    def __inform(self):
        pass


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.progress = 10

    def info(self):
        super().info()
        print(f"Name: {self.name}, Progress: {self.height}")

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.age = 35
    


s = Student("Ivan")
t = Teacher("Maks")

#s.info()
#t.info()



class Grandparent:
    def info(self):
        print("i'm grandparent")

class Parent(Grandparent):
    def info(self):
        print("i'm parent")

class Child(Parent):
    def __init__(self):
        super().info()




class Person:

    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
        self.height = 170

    def info(self):
        pass

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    

class Student(Person):
    def __init__(self, name, age, progress):
        super().__init__(name, age)
        self.progress = progress


student = Student("Nikita", 18, 12)
teacher = Teacher("Nazar", 55, 40000)

print(student.name)
print(student.age)
print(student.progress)

print(teacher.name)
print(teacher.age)
print(teacher.salary)