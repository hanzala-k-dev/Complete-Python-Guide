"""
Namespaces (LEGB) and decorators: scope resolution and function wrappers.
Show closures, timing, and type-check decorators with concise examples.
Inline examples demonstrate behavior and expected outputs.
"""

import time
import builtins


def demonstrate_namespaces_and_legb():
    x = "global"  # [LEGB] -> Output: demonstrates local/enclosing/global resolution

    def outer():
        x = "enclosing"  # [Enclosing] -> Output: shows enclosing scope

        def inner():
            x = "local"  # [Local] -> Output: print shows 'local'
            print(x)  # [Print Local] -> Output: 'local'

        inner()
        print(x)  # [Print Enclosing] -> Output: 'enclosing'

    outer()
    print(x)  # [Print Global] -> Output: 'global'
    print(len([1, 2, 3]))  # [Builtin len] -> Output: 3


def modify_global_variable():
    global a
    a = 2  # [Global assign] -> Output: sets global a to 2

    def temp():
        global a
        a += 1  # [Global modify] -> Output: increments global a

    temp()
    print(a)  # [Print Global] -> Output: 3


def demonstrate_nonlocal():
    def outer():
        a = 1  # [Enclosing init] -> Output: a starts at 1

        def inner():
            nonlocal a
            a += 1  # [Nonlocal modify] -> Output: increments enclosing a
            print("inner", a)  # [Print Inner] -> Output: 'inner 2'

        inner()
        print("outer", a)  # [Print Outer] -> Output: 'outer 2'

    outer()


def print_builtins():
    print(dir(builtins))  # [Builtins] -> Output: lists builtin names


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("***********************")  # [Decorator pre] -> Output: separator
        result = func(*args, **kwargs)
        print("***********************")  # [Decorator post] -> Output: separator
        return result

    return wrapper


@my_decorator
def hello():
    print("hello")  # [Hello] -> Output: 'hello' wrapped by separators


@my_decorator
def display():
    print("hello nitish")  # [Display] -> Output: 'hello nitish' wrapped by separators


def create_closure():
    def outer(outer_var):
        def inner():
            print(outer_var)  # [Closure inner] -> Output: prints captured value

        return inner

    return outer("Hello, world!")  # [Closure create] -> Output: returns inner bound to string


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # [Timer start] -> Output: records start time
        result = func(*args, **kwargs)
        print("time taken by", func.__name__, time.time() - start, "secs")  # [Timer end] -> Output: elapsed secs
        return result

    return wrapper


@timer
def delayed_hello():
    print("hello world")  # [Delayed hello] -> Output: prints 'hello world'
    time.sleep(2)  # [Sleep] -> Output: pauses ~2s


@timer
def square_with_timer(num):
    time.sleep(1)  # [Sleep] -> Output: pauses ~1s
    print(num**2)  # [Square] -> Output: prints square


@timer
def power(a, b):
    print(a**b)  # [Power] -> Output: prints a**b


def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if args and type(args[0]) == data_type:
                return func(*args, **kwargs)
            else:
                raise TypeError("Invalid datatype for this function")  # [Type Guard] -> Output: raises TypeError

        return inner_wrapper

    return outer_wrapper


@sanity_check(int)
def square(num):
    print(num**2)  # [Square Guarded] -> Output: prints square when input is int


@sanity_check(str)
def greet(name):
    print("hello", name)  # [Greet Guarded] -> Output: prints greeting when input is str


if __name__ == "__main__":
    print("--- Namespaces & LEGB ---")
    demonstrate_namespaces_and_legb()  # [Run] -> Output: shows LEGB prints

    print("\n--- Modifying Global ---")
    modify_global_variable()  # [Run] -> Output: prints 3

    print("\n--- Nonlocal Keyword ---")
    demonstrate_nonlocal()  # [Run] -> Output: prints inner and outer values

    print("\n--- Manual Decorators & @ Syntax ---")
    hello()  # [Run] -> Output: separators, 'hello', separators
    display()  # [Run] -> Output: separators, 'hello nitish', separators

    print("\n--- Closures ---")
    closure_func = create_closure()
    closure_func()  # [Run] -> Output: 'Hello, world!'

    print("\n--- Timer Decorator ---")
    delayed_hello()  # [Run] -> Output: prints and times (~2s)
    square_with_timer(2)  # [Run] -> Output: prints 4 and times (~1s)
    power(2, 3)  # [Run] -> Output: prints 8 and times

    print("\n--- Decorators with Arguments ---")
    square(2)  # [Run] -> Output: prints 4
    greet("nitish")  # [Run] -> Output: prints 'hello nitish'

    try:
        square("hehe")
    except TypeError as e:
        print(f"Caught expected error: {e}")  # [Error] -> Output: prints TypeError message
