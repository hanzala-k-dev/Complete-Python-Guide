"""Shows print behavior for literals, mixed types, separators, and newline control.
Includes string, numeric, boolean, and custom separator examples.
Demonstrates default line breaks and `end` continuation.
"""

print("Hello World!")  # [Literal Print] -> Output: Hello World!

print(8)  # [Integer Print] -> Output: 8

print(7.1)  # [Float Print] -> Output: 7.1

print(False)  # [Boolean Print] -> Output: False

print("Pakistan", "India", "Bangladesh", "Iran")  # [Multiple Args] -> Output: Pakistan India Bangladesh Iran

print("Pakistan", 5, True)  # [Mixed Types] -> Output: Pakistan 5 True

print("Pakistan", "India", "Bangladesh", "Iran", sep="/")  # [Custom Sep '/'] -> Output: Pakistan/India/Bangladesh/Iran

print("Pakistan", "India", "Bangladesh", "Iran", sep="-")  # [Custom Sep '-'] -> Output: Pakistan-India-Bangladesh-Iran

print("Hello")  # [Line Print 1] -> Output: Hello

print("World")  # [Line Print 2] -> Output: World

print("Hello", end="")  # [No Newline] -> Output: HelloWorld

print("World")  # [Continuation] -> Output: World
