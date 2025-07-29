from student import Student
from course import CourseGroup


student = Student("Анна", "Петрова", 24, "Инженер по тестированию")
classmate1 = Student("Елена", "Архипова", 27, "Инженер по тестированию")
classmate2 = Student("Олег", "Михайлов", 23, "Инженер по тестированию")
classmate3 = Student("Игорь", "Макаров", 19, "Инженер по тестированию")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])
print(course_group)
