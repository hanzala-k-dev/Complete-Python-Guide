"""
This file demonstrates Python functions with examples for default arguments, variable arguments, keyword arguments, scope,
nested functions, and function objects. Each example includes comments and output notes so learners can follow the behavior clearly.
"""


def is_even(number):
    # Return whether an integer is even or odd.
    if type(number) == int:
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Not allowed"


for i in range(1, 11):
    print(
        is_even(i)
    )  # prints Odd, Even, Odd, Even, Odd, Even, Odd, Even, Odd, Even for numbers 1 through 10

print(is_even.__doc__)  # prints the function docstring if present
print(print.__doc__)  # prints the documentation for built-in print()
print(type.__doc__)  # prints the documentation for built-in type()


def power(a=1, b=1):
    # Return a raised to the power of b using default arguments when not provided.
    return a**b


print(power(2, 3))  # 8
print(power(3, 2))  # 9
print(power(2))  # 2 because b defaults to 1
print(power())  # 1 because both a and b default to 1
print(power(b=2, a=3))  # 9, keyword arguments can be supplied out of order


def flexi(*numbers):
    # Multiply any number of positional arguments and print the input tuple.
    product = 1
    print(numbers)  # prints the tuple of all passed arguments
    print(type)  # prints the built-in type object
    for item in numbers:
        product *= item
    print(product)  # prints the product of all arguments


flexi(1)  # prints (1,) and 1
flexi(1, 2)  # prints (1, 2) and 2
flexi(1, 2, 3)  # prints (1, 2, 3) and 6
flexi(1, 2, 3, 4, 5, 6, 7, 8, 9)  # prints tuple and 362880


def multiply(*args):
    # Multiply all positional arguments and return the result.
    product = 1
    for item in args:
        product *= item
    print(args)  # prints the tuple of all passed arguments
    return product


print(
    multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12)
)  # prints arguments tuple and returns 3628800


def display(**kwargs):
    # Print keyword arguments as key -> value pairs.
    for key, value in kwargs.items():
        print(key, "->", value)


display(india="delhi", srilanka="colombo", nepal="kathmandu", pakistan="islamabad")
# Output:
# india -> delhi
# srilanka -> colombo
# nepal -> kathmandu
# pakistan -> islamabad

L = [1, 2, 3]
print(L.append(4))  # None because append changes the list in place
print(L)  # [1, 2, 3, 4]


def func_a():
    print("inside func_a:")


def func_b(y):
    print("inside func_b:")
    return y


def func_c(z):
    print("inside func_c:")
    return z()


print(func_a())  # prints inside func_a: and then None because func_a returns nothing
print(5 + func_b(2))  # prints inside func_b: and then 7
print(func_c(func_a))  # prints inside func_c:, inside func_a:, and then None


def f(y):
    x = 1
    x += 1
    print(x)  # prints 2


x = 5
f(x)
print(x)  # prints 5 because x outside the function is unchanged


def g(y):
    print(x)  # reads global x because there is no local assignment
    print(x + 1)  # prints 6 when x is 5


x = 5
g(x)
print(x)  # prints 5


def h_mod(y):
    global x
    x += 1  # modifies the global x variable


x = 5
h_mod(x)
print(x)  # prints 6 because global x was incremented


def f_scope(x):
    x += 1
    print("in f(x): x =", x)  # prints 4 when called with x=3
    return x


x = 3
z = f_scope(x)
print("in main program scope: z =", z)  # prints 4
print("in main program scope: x =", x)  # prints 3 because outer x stays the same


def f_nested():
    print("Inside f")

    def g_nested():
        print("Inside g")

    g_nested()


f_nested()  # prints Inside f then Inside g


def g_hard(x):
    def h():
        x = "abc"  # this x is local to h and does not affect outer x

    x += 1
    print("in g(x): x =", x)  # prints 4 when x starts as 3
    h()
    return x


x = 3
z = g_hard(x)


def g_comp(x):
    def h(x):
        x += 1
        print("in h(x): x =", x)  # prints 5 when called with x=4

    x += 1
    print("in g(x): x =", x)  # prints 4 when x starts as 3
    h(x)
    return x


x = 3
z = g_comp(x)
print("in main program scope: x =", x)  # prints 3
print("in main program scope: z =", z)  # prints 4


def f_obj(num):
    return num**2


print(f_obj(2))  # prints 4
print(f_obj(4))  # prints 16

x_alias = f_obj
print(x_alias(2))  # prints 4
print(x_alias(4))  # prints 16

del f_obj

print(x_alias(2))  # prints 4 because x_alias still refers to the function
print(type(x_alias))  # prints <class 'function'>

L = [1, 2, 3, 4, x_alias]
print(L)  # list includes the function object
print(L[-1](-3))  # prints 9 because x_alias(-3) returns (-3)**2

L = [1, 2, 3, 4, x_alias(5)]
print(L)  # prints [1, 2, 3, 4, 25]


def func_a_arg():
    print("inside func_a")


def func_c_arg(z):
    print("inside func_c")
    return z()


print(func_c_arg(func_a_arg))  # prints inside func_c and inside func_a, then None


def f_return():
    def x(a, b):
        return a + b

    return x


val = f_return()(3, 4)
print(val)  # prints 7


def square(num):
    return num**2


print(type(square))  # prints <class 'function'>
print(id(square))  # prints the unique id for square

x_sq = square
print(id(x_sq))  # same id as square before it was deleted
print(x_sq(3))  # prints 9

del square

L = [1, 2, 3, 4, x_sq]
print(L[-1](3))  # prints 9

s = {x_sq}
print(s)  # prints a set containing the function object
