class Student:
    def __init__(self):
        self.name = "Vlad"
        self.age = 18

    def Hello(self):
        print("Hello World")

s = Student()

s.Hello()

print(s.name)
print(s.age)