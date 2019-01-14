print("hello python")

def add_numbers(a, b):
    print(a + b)

add_numbers(5, 5)

# To convert foloat to int or vise versa
# call a funciton with prepended name of datatype 

print("Convert 3.14 to integer")
print(int(3.14))

print("Convert integer 10 to float")
print(float(10))

name = "Vladimir"
profession = "coder"

# string format function
print(f"I'm {name}. My lifestyle is a {profession}")

# check if truthy 

if name == "Vladimir" and profession == "coder":
    print("this will execute")

# ternary operator in python --- in JavaScript it would be
# console.log(name.length > profession.length ? "bigger" : "smaller")
print("bigger" if len(name) > len(profession) else "smaller")

# List manipulation/delete from right and left(-)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for loop(number is just a variable)
for number in list:
    print(f"number {number}")

# for loop with range - first argument defines = start interation index, secont argument defines = finish iteration index, third argument defines = increment(default == 1


some_number = 0
for number in range(1, 7, 2):
    print(f"for loop with start index = 1, finish index = 7, iterator = 2 {number}")

# add if condition in for loop and break which is going to stop loop after match
for number in list:
    if number == 5:
        print(f"Found number {number}")
        break
    print(f"Currently number is {number}")

# define Dictionary(equivalent of object in JavaScript)

student = {
    'name': "Vladimir",
    'language': "Phyton",
    'city': "Tampa"
}

# exeption block

try:
    last_name = student["last_name"]
# key error handling
except KeyError:
    print("Error finding last name")
print("eception works!!!!")

try:
    int_plus_string = 3 + name
# type error handling
except TypeError:
    print("can't add diff data types")

