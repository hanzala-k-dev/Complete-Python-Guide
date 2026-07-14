# FILE INPUT/OUTPUT (I/O) FOUNDATIONS IN PYTHON

# CHARACTERISTICS OF TEXT MODE ('w', 'a', 'r')

# Case 1: File writing basics (Overwrites or creates if absent)
f = open('sample.txt', 'w')
f.write('Hello world')
f.close()

# Attempting operations on closed descriptors yields an error
try:
    f.write('hello')
except ValueError as e:
    print(f"Caught expected error: {e}")

# Multiline explicit structural write
f = open('sample1.txt', 'w')
f.write('hello world')
f.write('\n how are you?')
f.close()

# Case 2: Standard overwriting behavior under write mode
f = open('sample.txt', 'w')
f.write('salman khan')
f.close()

# Append mode ('a') maintains file footprint while expanding strings
f = open('sample1.txt', 'a')
f.write('\nI am fine')
f.close()

# List sequence processing via .writelines()
L = ['hello\n', 'hi\n', 'how are you\n', 'I am fine']
f = open('sample.txt', 'w')
f.writelines(L)
f.close()


# READING INTERACTION METRICS (.read vs .readline)

# Loading entire file contents contextually as a cohesive sequence string
f = open('sample.txt', 'r')
s = f.read()
print(s)
f.close()

# Segmented slice retrieval using integer offsets
f = open('sample.txt', 'r')
s = f.read(10)
print(s)
f.close()

# Incremental lines processing mapping using step tracking pointers
f = open('sample.txt', 'r')
print(f.readline(), end='')
print(f.readline(), end='')
f.close()

# End-of-file condition processing loop patterns
f = open('sample.txt', 'r')
while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data, end='')
f.close()


# AUTOMATED RESOURCE TRACKING VIA CONTEXT MANAGERS

with open('sample1.txt', 'w') as f:
    f.write('selmon bhai')

try:
    f.write('hello')
except ValueError as e:
    print(f"Context manager safely closed file: {e}")

with open('sample.txt', 'r') as f:
    print(f.readline())

# Linear tracking inside step-buffered block allocations
with open('sample.txt', 'r') as f:
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))


# CHUNK-BASED STRATEGIES FOR OVERSIZED MEMORY STREAMS

big_L = ['hello world ' for _ in range(1000)]
with open('big.txt', 'w') as f:
    f.writelines(big_L)

with open('big.txt', 'r') as f:
    chunk_size = 10
    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end='***')
        f.read(chunk_size)
print()


# BUFFER CURSOR POSITION NAVIGATION (.seek AND .tell)

with open('sample.txt', 'r') as f:
    f.seek(15)
    print(f.read(10))
    print(f.tell())
    print(f.read(10))
    print(f.tell())

with open('sample.txt', 'w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('Xa')


# HANDLING TYPE CONSTRAINTS & BINARY BOUNDARIES

try:
    with open('sample.txt', 'w') as f:
        f.write(5)
except TypeError as e:
    print(f"Type enforcement error: {e}")

with open('sample.txt', 'w') as f:
    f.write('5')

with open('sample.txt', 'r') as f:
    print(int(f.read()) + 5)

d = {'name': 'nitish', 'age': 33, 'gender': 'male'}
with open('sample.txt', 'w') as f:
    f.write(str(d))

with open('sample.txt', 'r') as f:
    raw_str = f.read()
    try:
        print(dict(raw_str))
    except ValueError as e:
        print(f"String literal restructuring failed as expected: {e}")

# Emulating binary handling via generic mock sequence blocks
binary_payload = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
with open('screenshot1.png', 'wb') as f:
    f.write(binary_payload)

# Using 'rb' and 'wb' flags prevents text decoding failures
with open('screenshot1.png', 'rb') as f:
    with open('screenshot_copy.png', 'wb') as wf:
        wf.write(f.read())


# DATA STRUCTURE PERSISTENCE VIA NATIVE JSON FORMATTING
import json

L_json = [1, 2, 3, 4]
with open('demo.json', 'w') as f:
    json.dump(L_json, f)

d_json = {'name': 'nitish', 'age': 33, 'gender': 'male'}
with open('demo.json', 'w') as f:
    json.dump(d_json, f, indent=4)

with open('demo.json', 'r') as f:
    d_loaded = json.load(f)
    print(d_loaded)
    print(type(d_loaded))

t_tuple = (1, 2, 3, 4, 5)
with open('demo.json', 'w') as f:
    json.dump(t_tuple, f)

with open('demo.json', 'r') as f:
    t_loaded = json.load(f)
    print(t_loaded)
    print(type(t_loaded))  # Deserializes as a list primitive type

d_nested = {'student': 'nitish', 'marks': [23, 14, 34, 45, 56]}
with open('demo.json', 'w') as f:
    json.dump(d_nested, f)


# CUSTOM OBJECT ENCODING SPECIFICATIONS (JSON EXTRACTION)

class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

person_instance = Person('Nitish', 'Singh', 33, 'male')

def serialize_to_string(obj):
    if isinstance(obj, Person):
        return f"{obj.fname} {obj.lname} age -> {obj.age} gender -> {obj.gender}"

with open('demo.json', 'w') as f:
    json.dump(person_instance, f, default=serialize_to_string)

def serialize_to_dict(obj):
    if isinstance(obj, Person):
        return {'name': f"{obj.fname} {obj.lname}", 'age': obj.age, 'gender': obj.gender}

with open('demo.json', 'w') as f:
    json.dump(person_instance, f, default=serialize_to_dict, indent=4)

with open('demo.json', 'r') as f:
    custom_loaded = json.load(f)
    print(custom_loaded)
    print(type(custom_loaded))


# SYSTEM OBJECT SERIALIZATION THROUGH PICKLING PROTOCOLS
import pickle

class PicklePerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Hi my name is {self.name} and I am {self.age} years old")

p_pickle = PicklePerson('nitish', 33)

with open('person.pkl', 'wb') as f:
    pickle.dump(p_pickle, f)

with open('person.pkl', 'rb') as f:
    p_unpickled = pickle.load(f)

p_unpickled.display_info()