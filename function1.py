# def hello_func(greeting, name = "you"):
#     return f"{greeting} {name}"
# print(hello_func("hi", name="Allen"))

def student_info(*args, **kwargs):
    
    print(args)
    print(kwargs)

course = ['math', 'art']
info = {'name': 'Allen', 'age': 18}
student_info(*course, **info)



