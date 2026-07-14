"""Shows conditional flow for credential checks, value comparison, and menu choices.
The examples use if/elif/else to demonstrate branching behavior.
Outputs are annotated to clarify learner expectations.
"""

# --- Email and password validation (simple example) ---
email = input("Enter your email: ")

if "@" in email:
    # Prompt for password only if email contains '@'
    password = input("Enter your password: ")

    # Check credentials (hard-coded for demonstration only)
    if email == "hanzala@gmail.com" and password == "1234":
        print("Welcome")  # Output: Welcome
    elif email == "hanzala@gmail.com" and password != "1234":
        print("Invalid password")  # Output: Invalid password
        # Give the user one more chance
        password = input("Enter your password: ")
        if password == "1234":
            print("Finally correct")  # Output: Finally correct
        else:
            print("Invalid password")  # Output: Invalid password
    else:
        print("Invalid credentials")  # Output: Invalid credentials
else:
    print("Invalid email format")  # Output: Invalid email format


# --- Find the smallest of three numbers ---
# Read three integers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print("smallest number is:", a)  # Output: smallest number is: <a>
elif b < c:
    print("smallest number is:", b)  # Output: smallest number is: <b>
else:
    print("smallest number is:", c)  # Output: smallest number is: <c>


# --- Simple menu using if/elif/else ---
menu = input("""How can I help you?
1. pin change
2. balance check
3. withdraw
4. exit
""")

if menu == "1":
    print("pin change")  # Output: pin change
elif menu == "2":
    print("balance check")  # Output: balance check
elif menu == "3":
    print("withdraw")  # Output: withdraw
else:
    print("exit")  # Output: exit
