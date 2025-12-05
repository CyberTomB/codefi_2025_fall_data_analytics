print("Hello, world!")

# int: 69
# float: 6.9
# string: "Hello, world"
# bool: True/False
# null: 

age = 32
name = "Tom"
height = 6.1
is_teacher = True

age += 1

print(f"Hi, I'm {name} and I'm {age} years old!")

# + addition
# - substraction
# / division
# * multiplication
# ** exponent
# % modulus

hello = "Hello World"
print(hello.lower())

print(hello)

hello = hello.replace("World", "Students!")
print(hello)

def greet(name):
    print(f"Hello, {name}!")

def add_together(a, b):
    return a + b

x = -3
def figure_out_number(number):
    if number > 2:
        print("X is greater than 2!")
    elif number < 0:
        print("No negative numbers here!")
    else:
        print("X is not greater than 2")

# 0 = apple, 1 = banana, 2 = orange
fruits = ["apple", "banana", "orange"]

fruits.append("pear")
fruits.append("grape")
# fruits.pop()

first = 2
second = 3


for i in [first, second]:
    print(f"fruits[{i}]")
    print(fruits[i])

person = {
    "name": "Tom",
    "age": 32,
    "num_students": 2,
    "anything_we_want": "whatever"
}

for k in person.keys():
    greet(person[k])