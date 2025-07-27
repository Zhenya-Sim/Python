class Student:
    def __init__(self, f_name, l_name, age, course):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.age} {self.course}"
