import math

width = 104.32
height = 15.654
area = width * height
message = f"The area of a rectangle with a width of {width} and a height of {height} is {area:.2f}."
print(message)

r = 50
print(f"A circle with radius {r} has an area of {math.pi * r * r:.2f}")
print(message)

name1 = "John"
age1 = 25
print(f"{name1:15} - {age1:10}")

name2 = "Alice"
age2 = 30
print(f"{name2:15} - {age2:10}")

name = "John"
age = 25.456
print(f"{name: >20} - ${age: >20.2f}")

r = 52
area = 3.14159 * r**2
output = "The area of a circle with a radius of {} is {:.2f} square units.".format(r, area)
print(output)

name = "John"
age = 25
output = "{name:@^15} - {age:#^10}".format(name=name, age=age)
print(output)
print("Name is %s, and age is %.2f" % (name, age))
print(name.rjust(15), " - ", str(age).center(10))
print(f"{name:>15} - {age:^10}")

with open('info.txt', 'r') as file:

    contents = file.read()
    print(contents)














