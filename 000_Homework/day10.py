## 1. Iterate 0 to 10 using for loop, do the same using while loop.

# for i in range(0, 11):
#     print(i)
#
# print("\nNow while loop\n")
# n = 0
# while n < 11:
#     print(n)
#     n += 1

##2. Iterate 10 to 0 using for loop, do the same using while loop.

# nums = list(range(0, 11))
# print(type(nums))
# nums = nums[::-1]
#
# for i in nums:
#     print(i)

# nums = list(range(11))
# print(nums)

# for i in range(11, 0, -1):
#     print(i)
#
#
# print("\nNow while loop\n")
# n = 10
# while n >= 1:
#     print(n)
#     n -= 1


## 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""
#
##
###
####
#####
######
#######

"""

# stars = "#"
#
# for i in range(7):
#     print(stars)
#     stars += "#"

##4. Use nested loops to create the following:
"""

   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
"""


# for i in range(8):
#     for j in range(8):
#         print("# ", end=" ")
#     print()

##5. Print the following pattern:
"""
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100

"""

# for i in range(11):
# print(f"{i} x {i} = ", i * i)

## Write code that prints the following pattern of coordinates:
"""
    (0,0) (0,1) (0,2)
    (1,0) (1,1) (1,2)
    (2,0) (2,1) (2,2)
"""

# for i in range(3):  # rows
# for j in range(3):  # columns
#     print(f"({i},{j})", end=" ")
# print()

## 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lists = ["Python", "Numpy", "Pandas", "Django", "Flask"]

# for i in lists:
#     print(i)
#
## 7. Use for loop to iterate from 0 to 100 and print only even numbers
#
# for i in range(101):
#     if i % 2 == 0:
#         print(i)
#
## Write a program that prints all the numbers from 1 to 50,
## but for multiples of 3, print "Fizz",
####for multiples of 5, print "Buzz",
##and for numbers that are multiples of both 3 and 5, print "FizzBuzz".

# for i in range(1, 16):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#

## Write a program that prints this right-angled triangle made of numbers:
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#
## Write a program that prints this number pyramid:
"""
1
22
333
4444
55555

"""

# for i in range(1, 6):
#     for j in range(i, 6):
#         print(i, end="")
#     print()


## 8. Use for loop to iterate from 0 to 100 and print only odd numbers

# for i in range(0, 101):
#     if i % 2 == 1:
#         print(i)
#

## 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#
# nums = 0
# for i in range(0, 101):
#     nums += i
# print("The sum of all numbers is: ", nums)
#
# ##1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# evens = 0
# odds = 0
#
# for i in range(0, 101):
#     if i % 2 == 0:
#         evens += i
#     else:
#         odds += i
# print("Total sum of all even is: ", evens)
# print("Total sum of all odds is: ", odds)


## 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file.
## Loop through the countries and extract all the countries containing the word _land_.
# import os
# import sys
#
# sys.path.append("..")
# from data.countries import countries
#
# # print(countries)
#
# countries_with_land = []
#
# for i in countries:
#     if "land" in i:
#         countries_with_land.append(i)
#
# print(countries_with_land)


## 1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# fruits = ["banana", "orange", "mango", "lemon"]
# reversed_fruits = []
# for i in fruits:
#     reversed_fruits.insert(0, i)
# print(reversed_fruits)


# 2. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.
#    1. What are the total number of languages in the data
#    2. Find the ten most spoken languages from the data
#    3. Find the 10 most populated countries in the world

import os
import sys

sys.path.append("..")

# print(data[0])
# print(data[0:2])
from collections import Counter

from data.countries_data import data

# print(data)

# 1.
# total_languages = []
#
# for i in data:
#     for j in i["languages"]:
#         total_languages.append(j)
# # print(len(total_languages))
#
# # 2.
# langugage_count = {}
# for language in total_languages:
#     if language in langugage_count:
#         langugage_count[language] += 1
#     else:
#         langugage_count[language] = 1
#
# # print(langugage_count)
#
# sorted_languages = sorted(langugage_count.items(), key=lambda x: x[1], reverse=True)
#
# for i in range(min(10, len(sorted_languages))):
#     lang, count = sorted_languages[i]
#     print(f"{lang}: {count}")
#
#
# 3. Find the 10 most populated countries in the world

# print(data[0:2])

count_pop = {}
#
# for i in data:
#     count_pop[i["name"]] = i["population"]
# print(count_pop)
#
# sorted_count = sorted(count_pop.items(), key=lambda x: x[1], reverse=True)
# # print(sorted_count)
#
# for i in range(min(10, len(sorted_count))):
#     country, pop = sorted_count[i]
#     print(f"{country}: {pop}")


i = {"name": "Afghanistan", "population": 27657145}

count_pop[i["name"]] = i["population"]
print(count_pop)
