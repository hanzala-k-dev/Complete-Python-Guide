"""This file demonstrates Python dictionaries and their common operations.

It shows creation, access, modification, deletion, iteration, and
dictionary comprehensions with output notes for learning.
"""

# Empty dictionary
D = {}
print(D)  # {}

# Dictionary with string keys
D = {"Name": "Hanzala", "Gender": "Male"}
print(D)  # {'Name': 'Hanzala', 'Gender': 'Male'}

# Dictionary using a tuple as a key
D1 = {(1, 2, 3): "Hanzala"}
print(D1)  # {(1, 2, 3): 'Hanzala'}

# Duplicate keys keep the last assignment
D2 = {"Name": "Natty", "Name": "Maru"}
print(D2)  # {'Name': 'Maru'}

# Nested dictionary example
D3 = {"Name": "Hanzala", "College": "SGT", "Marks": {"M1": 99, "DS": 97, "Eng": 98}}
print(
    D3
)  # {'Name': 'Hanzala', 'College': 'SGT', 'Marks': {'M1': 99, 'DS': 97, 'Eng': 98}}

# Another nested structure with lowercase keys
s = {
    "name": "rauf",
    "college": "bit",
    "sem": 4,
    "subjects": {"dsa": 50, "maths": 67, "english": 34},
}
print(s)  # nested dictionary printed in insertion order

# Dictionary with tuple and string keys
D4 = {"name": "rauf", (1, 2, 3): 2}
print(D4)  # {'name': 'rauf', (1, 2, 3): 2}

# Create dictionary using dict() and a list of pairs
D5 = dict([("name", "rauf"), ("age", 32), (3, 3)])
print(D5)  # {'name': 'rauf', 'age': 32, 3: 3}

# Access values by key
D = {"Name": "Hanzala", "Gender": "Male"}
print(D["Name"])  # Hanzala
print(D.get("Name"))  # Hanzala
print(D["Gender"])  # Male
print(D.get("Gender"))  # Male

# Access nested dictionary values
D3 = {"Name": "Hanzala", "College": "SGT", "Marks": {"M1": 99, "DS": 97, "Eng": 98}}
print(D3["Marks"]["DS"])  # 97

# Modify values in a dictionary
D["Name"] = "Saad"
print(D)  # {'Name': 'Saad', 'Gender': 'Male'}

# Modify nested dictionary value
D3["Marks"]["DS"] = 10
print(D3)  # nested 'DS' value updated to 10

# Add new key-value pairs
D["Age"] = 22
print(D)  # {'Name': 'Saad', 'Gender': 'Male', 'Age': 22}

D3["Marks"]["M2"] = 95
print(D3)  # new nested key 'M2' added

# Delete an empty dictionary variable
D5 = {}
del D5

# pop removes a key and returns its value
D = {"Name": "Saad", "Gender": "Male", "Age": 22}
print(D.pop("Name"))  # Saad
print(D.popitem())  # removes and returns the last inserted pair, e.g. ('Age', 22)
print(D)  # remaining dictionary

# Delete a key using del
D = {"Name": "Saad", "Gender": "Male"}
del D["Gender"]
print(D)  # {'Name': 'Saad'}

# clear removes all items
D.clear()
print(D)  # {}

# Iterating through dictionary keys
D3 = {
    "Name": "Hanzala",
    "College": "SGT",
    "Marks": {"M1": 99, "DS": 10, "Eng": 98, "M2": 95},
}
for i in D3:
    print(i)  # prints each key in insertion order

for i in D3:
    print(i, D3[i])  # prints key and value pairs

# Membership tests on dictionary keys
print("Hanzala" in D3)  # False, checks keys only
print("Name" in D3)  # True

# Dictionary size and sorted keys
print(len(D3))  # 3
print(min(D3))  # 'College' (lexicographically smallest key)
print(max(D3))  # 'Name' (lexicographically largest key)
print(sorted(D3))  # ['College', 'Marks', 'Name']
print(sorted(D3, reverse=True))  # ['Name', 'Marks', 'College']

# Items, keys, and values views
print(
    D3.items()
)  # dict_items([('Name', 'Hanzala'), ('College', 'SGT'), ('Marks', {...})])
print(D3.keys())  # dict_keys(['Name', 'College', 'Marks'])
print(D3.values())  # dict_values(['Hanzala', 'SGT', {...}])

# Update dictionary with another dictionary
d1 = {1: 2, 3: 4, 4: 5}
d2 = {4: 7, 6: 8}
d1.update(d2)
print(d1)  # {1: 2, 3: 4, 4: 7, 6: 8}

# Dictionary comprehension examples
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

D = {"Name": "Rauf", "Gender": "Male", "Age": 30}
print(D.items())  # dict_items([('Name', 'Rauf'), ('Gender', 'Male'), ('Age', 30)])

# Filter comprehension based on key length
D1 = {key: value for key, value in D.items() if len(key) > 3}
print(D1)  # {'Name': 'Rauf', 'Gender': 'Male'}

# Create dictionary from a list
L = [1, 2, 3, 4, 5, 6, 7]
D2 = {item: item**2 for item in L}
print(D2)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

# Comprehension with condition
D2 = {item: item**2 for item in L if item % 2 == 0}
print(D2)  # {2: 4, 4: 16, 6: 36}

# Inline dictionary comprehension
print({i: i**2 for i in range(1, 11)})  # {1: 1, 2: 4, ..., 10: 100}

# Convert distances using dictionary comprehension
distances = {"karachi": 1000, "lahore": 2000, "islamabad": 3000}
print(
    distances.items()
)  # dict_items([('karachi', 1000), ('lahore', 2000), ('islamabad', 3000)])

converted_distances = {key: value * 0.62 for (key, value) in distances.items()}
print(converted_distances)  # {'karachi': 620.0, 'lahore': 1240.0, 'islamabad': 1860.0}

# Create a dictionary from two lists using zip
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]
weekly_temps = {i: j for (i, j) in zip(days, temp_C)}
print(weekly_temps)  # mapping of days to temperatures

# Filter dictionary by value
products = {"phone": 10, "laptop": 0, "charger": 32, "tablet": 0}
in_stock = {key: value for (key, value) in products.items() if value > 0}
print(in_stock)  # {'phone': 10, 'charger': 32}

# Nested dictionaries with multiplication tables
tables = {i: {j: i * j for j in range(1, 11)} for i in range(2, 5)}
print(tables)  # {2: {...}, 3: {...}, 4: {...}}
