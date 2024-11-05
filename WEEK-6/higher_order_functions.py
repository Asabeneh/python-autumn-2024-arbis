# Higher order function: it takes another function as a parameter
# It returns another function

def make_square(x):
    return x * x 


def make_cube(x, fn):
    return fn(x) * x

print(make_cube(2, make_square))
print(make_cube(3, make_square))
print(make_cube(10, make_square))

def add_nums(a, b):
    return a  + b

""" def do_math(a, b, operation):
    def add_nums():
        return a  + b
    def multiply():
        return a * b 
    def square():
        return a * a 
    if operation == 'add':
        return add_nums
    elif operation == 'multiply':
        return multiply 
    elif operation == 'square':
        return square
    else:
        pass 
    
print(do_math(2, 3, 'square')()) """


def do_math(a, b):
    def add_nums():
        return a  + b
    def multiply():
        return a * b 
    def square():
        return a * a 
    
    return {
       'add':add_nums,
       'multiply':multiply,
       'square':square
   }
    
print(do_math(2, 3)['add']())
print(do_math(10, 20)['multiply']())
print(do_math(10, 20)['square']())
    
    
        

    