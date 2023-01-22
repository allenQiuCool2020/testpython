def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper

@f1
def f(a, b):
    print(a, b)

# f = f1(f)

# f()
f("hi", {"a": 1})
@f1
def add(x, y):
    return x + y
print(add(2,3))