## ********Day 55 Start**********

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


# Creating dictionary with **kwargs:
def dicti(**kwargs):
    return kwargs

dict_i = dicti(age=12, name="poca", city="istanbul")
print(dict_i)
print(type(dict_i))

# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        summ = function(*args)
        print(f"You called {function.__name__}({args})\nIt returned {summ}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(a_function(1, 2, 3))