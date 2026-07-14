"""Show common Python string operations and examples.

Demonstrates string creation, slicing, comparison,
iteration, formatting, and basic search/replace operations.
"""

# Different ways to define string literals
c = "Hello"
print(c)  # Output: Hello

c = "Hello"
print(c)  # Output: Hello

# Using quotes inside strings
print("It's raining outside")  # Output: It's raining outside

c = """Hello"""
print(c)  # Output: Hello

c = """Hello"""
print(c)  # Output: Hello

c = str("Hello")
print(c)  # Output: Hello

# Indexing strings
c = "hello"
print(c)  # Output: hello
print(c[0])  # first character -> Output: h
print(c[-1])  # last character -> Output: o

# Slicing strings
c = "Hello World"
print(c)  # Output: Hello World
print(c[0:5])  # first five characters -> Output: Hello
print(c[2:])  # from index 2 to end -> Output: llo World
print(c[:4])  # up to index 4 (exclusive) -> Output: Hell
print(c[:])  # the whole string -> Output: Hello World
print(c[2:6:2])  # step by 2 -> Output: lo
print(c[0:8:3])  # Output: HlW
print(c[0:6:-1])  # empty because start < stop for negative step -> Output:
print(c[-5:-1:2])  # Output: ol
print(c[::-1])  # reverse string -> Output: dlroW olleH
print(c[-1:-5:-1])  # Output: dlro

# Concatenation and repetition
string1 = "Hello"
string2 = "World"
new_string = string1 + " " + string2
print(new_string)  # Output: Hello World

another_string = string1 + ", how are you?"
print(another_string)  # Output: Hello, how are you?

second_string = string1 + "this is my" + string2
print(second_string)  # Output: Hellothis is myWorld

print("*" * 50)  # Output: 50 asterisks
print("Hello" * 4)  # Output: HelloHelloHelloHello

# String comparison and logical operators
print("Hello" == "World")  # Output: False
print("Hello" != "World")  # Output: True
print("karachi" > "lahore")  # Output: True
print("karachi" < "karachi")  # Output: False
print("Hello" and "World")  # Output: World
print("" and "Hello")  # Output:
print("Hello" or "World")  # Output: Hello
print(not "Hello")  # Output: False

# Iterate over string characters
c = "Hello World"
for ch in c:
    print(ch)  # Output: each character in Hello World

for ch in c[2:7]:
    print(ch)  # Output: characters llo W

for ch in c[2:7:2]:
    print(ch)  # Output: l o

for ch in c[::-1]:
    print(ch)  # Output: each character in reversed Hello World

# Membership tests
print(c)  # Output: Hello World
print("H" in c)  # Output: True
print("h" in c)  # Output: False
print("World" not in c)  # Output: False

# String built-in functions
c = "Multan"
print(len(c))  # Output: 6
print(max(c))  # Output: u
print(min(c))  # Output: M
print(sorted(c))  # Output: ['M', 'a', 'l', 'n', 't', 'u']
print(sorted(c, reverse=True))  # Output: ['u', 't', 'n', 'l', 'a', 'M']

c = "Karachi"
print(c)  # Output: Karachi
print(c.capitalize())  # Output: Karachi
print("it is raining today".capitalize())  # Output: It is raining today
print("it is raining today".title())  # Output: It Is Raining Today
print(c.upper().lower())  # Output: karachi
print("KoLkAtA".swapcase())  # Output: kOlKaTa

# Count and search operations
print("it is raining".count("i"))  # Output: 3
print("it is raining".count("ing"))  # Output: 1
print("it is raining".count("x"))  # Output: 0
print("it is raining".find("i"))  # Output: 2
print("it is raining".find("g"))  # Output: 10
print("it is raining".find("raining"))  # Output: 3
print("it is raining".find("x"))  # Output: -1
print("it is raining".index("raining"))  # Output: 3
# The following would raise ValueError if uncommented:
# print("it is raining".index("x"))

print("it is raining".endswith("ing"))  # Output: True
print("it is raining".endswith("ingf"))  # Output: False
print("it is raining".startswith("it"))  # Output: True

# String formatting
print(
    "Hello my name is {} and I am {}".format("Hanzala", 20)
)  # Output: Hello my name is Hanzala and I am 20
print(
    "Hello my name is {1} and I am {0}".format("Hanzala", 20)
)  # Output: Hello my name is 20 and I am Hanzala
print(
    "Hello my name is {name} and I am {age}".format(name="Hanzala", age=20)
)  # Output: Hello my name is Hanzala and I am 20
print(
    "Hello my name is {age} and I am {name}".format(name="Hanzala", age=20)
)  # Output: Hello my name is 20 and I am Hanzala
print(
    "Hello my name is {name} and I am {name}".format(name="Hanzala", age=20, weight=80)
)  # Output: Hello my name is Hanzala and I am Hanzala

# Splitting and joining strings
print(
    "who is the pm of pakistan".split()
)  # Output: ['who', 'is', 'the', 'pm', 'of', 'pakistan']
print(
    "who is the pm of pakistan".split("pm")
)  # Output: ['who is the ', ' of pakistan']
print(
    "who is the pm of pakistan".split("i")
)  # Output: ['who ', 's the pm of pak', 'stan']
print("who is the pm of pakistan".split("x"))  # Output: ['who is the pm of pakistan']
print(
    " ".join(["who", "is", "the", "pm", "of", "pakistan"])
)  # Output: who is the pm of pakistan
print(
    "-".join(["who", "is", "the", "pm", "of", "pakistan"])
)  # Output: who-is-the-pm-of-pakistan

# Replace
print("Hi my name is Hanzala".replace("Hanzala", "Rauf"))  # Output: Hi my name is Rauf

# Strip
name = "          Hanzala           "
print(name)  # Output:           Hanzala
cleaned = name.strip()
print(cleaned)  # Output: Hanzala

# Count length manually
s = input("Enter a string: ")
counter = 0
for _ in s:
    counter += 1
print("Length of string:", counter)  # Output: Length of string: <length>

# Search for a character in the string
s = input("Enter a string: ")
term = input("What would you like to search: ")
counter = 0
for ch in s:
    if ch == term:
        counter += 1
print("Frequency:", counter)  # Output: Frequency: <count>

# Remove characters matching term from the string
s = input("Enter a string: ")
term = input("What would you like to remove: ")
result = ""
for ch in s:
    if ch != term:
        result += ch
print(result)  # Output: original string without term characters
