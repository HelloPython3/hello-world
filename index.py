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
# console.log(name.length > profession.length ? 'bigger' : 'smaller')
print('bigger' if len(name) > len(profession) else 'smaller')

# List manipulation/delete from right and left(-)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for loop(number is just a variable)
for number in list:
    print(f"number {number}")
