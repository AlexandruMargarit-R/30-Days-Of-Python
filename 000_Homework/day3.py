## Declare your age as integer variable
age = 30

# Declare your height as a float variable
height = 174.5

# Declare a variable that store a complex number
complex_nr = 1 + 1j
# print(complex_nr)

## Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
input_base = int(input("Enter base: "))
input_height = int(input("Enter height: "))
triangle_area = 0.5 * input_base * input_height
print("The area of the triangle is ", triangle_area)

## Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is ", perimeter)

## Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter rectangle length "))
width = int(input("Enter rectangle width "))
area = length * width
print("The area of rectangle is ", area)
perimeter = 2 * (length + width)
print("The perimeter of rectangle is ", perimeter)

## Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = float(input("Enter circle radius: "))
area = pi * radius**2
circumference = 2 * pi * radius
print("Area is: ", area)
print("Circumference is: ", circumference)

## Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2
slope_8 = m
y_intercept = b
x_intercept = -b / m
#
print(f"Equation: y = {slope_8}x + {y_intercept}")
print(f"Slope: {slope_8}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

## Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import math

p1 = (2, 2)
p2 = (6, 10)

x1, y1 = p1
x2, y2 = p2
slope_9 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Point 1:", p1)
print("Point 2:", p2)
print("Slope is", slope_9)
print("Distance is", distance)

## Compare the slopes in tasks 8 and 9.
print("Comparing slope 8 vs 9", slope_8 == slope_9)
#
#
## Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = 0
y = x**2 + 6 * x + 9

while y != 0:
    x -= 1
    y = x**2 + 6 * x + 9
print("y is 0 when x is: ", x)

## Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len("python"))
print(len("dragon"))

print("python" == "dragon")

## Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("on" in ("python" and "dragon"))

## I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentance = "I hope this course is not full of jargon"
print("jargon" in sentance)

## There is no 'on' in both dragon and python

print("on" not in ("dragon" and "python"))

## Find the length of the text python and convert the value to float and convert it to string

print(type(str(float(len("python")))))

## Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

x = 2

if x % 2 == 0:
    print("even")
else:
    print("odd")

## Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

int_nr = int(2.7)
flr_div = 7 // 3

print(int_nr)
print(flr_div)
print(flr_div == int_nr)

## Check if type of '10' is equal to type of 10

print("10" == 10)

## Check if int('9.8') is equal to 10
int_nr = int(float("9.8"))
print(int_nr == 10)

## Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input("Enter hours: "))
rate = int(input("Enter rate/hour: "))

print("Your weekly earning is: ", hours * rate)

## Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter number of years: "))
seconds = years * 31556952

if years > 100:
    print("A person can leave 100 years")
else:
    print(f"You have lived for {seconds} seconds")

## Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")
