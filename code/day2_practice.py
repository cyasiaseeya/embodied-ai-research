# Variables - a name that stores a value and lets you reuse it

name = "Sia"
age = 25
score = 9.5
is_tired = True

print(name)
print("Hello, " + name)

# Lists - a collection of items in order

fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4]

print(fruits)
print(fruits[0])
fruits.append("kiwi")
print(fruits)

# Dictionary - stores data as key: value

person = {
    "name": "Sia",
    "age": 25
}
print(person["name"])
person["city"] = "Seoul"
print(person)

# Functions - a reusable block of code

def greet(name):
    print("Hello, ", name)

greet(name)
greet("Min")

def add(a, b):
    return a + b

result = add(2, 3)
print(result)

# Loops - repeats code

for number in numbers:
    print(number)

# If statements - checks a condition

age = 5
if age >= 10:
    print("Old enough")
else:
    print("Not old enough")

# Importing Libraries - gives you extra tools to work with

import math

print(math.sqrt(16))

import random

print(random.randint(1, 10))

# Reading and writing files

with open("day2_notes.txt", "r") as file:
    text = file.read()

print(text)

message = "I finished my Python review"

with open("day2_notes.txt", "w") as file:
    file.write(message)
