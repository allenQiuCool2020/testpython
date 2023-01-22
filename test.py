# 	print(a)
# a = 1
# if a > 0:
# import sys
# print (sys.executable)
# print('a')
# print(sys.version)

# x = 1
# print(type("hello"))
# print(type(x))
# def hello():
# 	print("hello")

# print(type(hello))




# from unittest import result


# class Dog:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print(name)

# 	def get_name(self):
# 		return self.name

# 	def get_age(self):
# 		return self.age

# 	def	set_age(self, age):
# 		self.age = age
# 		return self.age

# 	def meow(self):
# 		return "meow"

# 	def bark(self):
# 		print('bark')

# 	def add_one(self, x):
# 		return x + 1

# d = Dog('Jack', 10)
# print(d.get_name())
# print(d.set_age(20))
# print(d.set_age(21))



# d.bark()
# print(type(d))

# a = d.add_one(6)
# print(a)

# d1 = Dog('Tom', 10)
# print(d1.get_name())


class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade # 0-100

	def get_grade(self):
		return self.grade

class Course:
	def	__init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []
	
	def add_student(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False
	
	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()
		return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Allen", 20, 99)
s3 = Student("Tom", 21, 78)

course = Course('Science', 2)

course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))

print(course.students)
print(course.students[0].name) 

print(course.get_average_grade())