## 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
# def add_two_numbers(a, b):
#     total = a + b
#     return total
#
#
# print(add_two_numbers(1, 2))
#
# ## 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.


# def area_of_circle(r):
#     area = 3.14 * r * r
#     return area
#
#
# print(area_of_circle(2))


## 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
##Check if all the list items are number types. If not do give a reasonable feedback.


# def add_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
#
#
# print(add_all_nums(2, 3))


##4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
# def convert_celsius_to_fahrenheit(c):
#     f = (c * 9 / 5) + 32
#     return f
#
#
# print(convert_celsius_to_fahrenheit(20))
#
# ## 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def check_seasons(month):
#     Spring = ["mar", "apr", "may"]
#     Summer = ["june", "july", "aug"]
#     Autumn = ["sept", "oct", "nov"]
#     Winter = ["dec", "jan", "feb"]
#     if month in Spring:
#         return "Spring"
#     elif month in Summer:
#         return "Summer"
#     elif month in Autumn:
#         return "Autumn"
#     elif month in Winter:
#         return "Winter"
#
#
# print(check_seasons("mar"))


# def check_seasons(month):
#     seasons = {
#         "Spring": ["mar", "apr", "may"],
#         "Summer": ["june", "july", "aug"],
#         "Autumn": ["sept", "oct", "nov"],
#         "Winter": ["dec", "jan", "feb"],
#     }
#
#     for season, months in seasons.items():
#         if month in months:
#             return season
#
#     return "Unknown month"
#
#
# print(check_seasons("kas"))
#
##6. Write a function called calculate_slope which return the slope of a linear equation

# def calculate_slope(*args):
#     if len(args) != 4:
#         raise ValueError("Please provide exactly four values: x1, y1, x2, y2")
#
#     x1, y1, x2, y2 = args
#
#     if x2 == x1:
#         return None  # undefined slope for vertical line
#
#     m = (y2 - y1) / (x2 - x1)
#     return m
#
# print(calculate_slope(1, 2, 3, 4))  # Output: 1.0


##  8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(*args):
#     for i in args:
#         print(i)
#
#
# lst = [1, 2, 3, 4, 5, 6]
# print_list(*lst)


##9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).


# def reverse_list(a):
#     reversed_list = []
#     for i in a:
#         reversed_list.insert(0, i)
#     return reversed_list
#
#
# # fruits = ["apple", "pear", "banana"]
# abc = ["A", "B", "C"]
# print(reverse_list(abc))
# #
#
## 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(lst):
#     capiltalized_items = []
#     for i in lst:
#         capiltalized_items.append(i.capitalize())
#     return capiltalized_items
#
# fruits = ["apple", "pear", "banana"]
# print(capitalize_list_items(fruits))
#
##11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
"""
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
"""


# def add_item(lst, item):
#     lst.insert(lst[-1], item)
#     return lst
#
#
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 11))

## 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
"""
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
"""


# def remove_item(lst, item):
#     lst.remove(item)
#     return lst
#
#
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]

##13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
"""
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
"""


# def sum_of_numbers(number):
#     numbers_lst = []
#     for n in range(0, number + 1):
#         numbers_lst.append(n)
#     return sum(numbers_lst)
#
#
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10))  # 55
# print(sum_of_numbers(100))  # 5050
#
# # n = 10
# # print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)


## 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds(num):
#     summed_odd = []
#     for i in range(1, num + 1):
#         if i % 2 == 1:
#             summed_odd.append(i)
#
#     return sum(summed_odd)
#
#
# print(sum_of_odds(0))

## 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_even(num):
#     summed_even = []
#     for i in range(0, num + 1):
#         if i % 2 == 0:
#             summed_even.append(i)
#
#     return sum(summed_even)
#
#
# print(sum_of_even(4))

##1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
"""
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
"""
# def even_and_odds(n):
#     even_count = 0
#     odd_count = 0
#     if n < 0:
#         return "Positive numbers only"
#     else:
#         for i in range(0, n + 1):
#             if i % 2 == 0:
#                 even_count += 1
#             else:
#                 odd_count += 1
#     return f"""the number chosen is: {n}
# The number of odds is {odd_count}
# The number of even is {even_count}"""
#
#
# print(even_and_odds(100))

## 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


# def factorial(n):
#     factorial_number = 1
#     for i in range(1, n + 1):
#         factorial_number *= i
#     return factorial_number
#
#
# print(factorial(6))

## 1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode,
##calculate_range, calculate_variance, calculate_std (standard deviation).

# numbers = [3, 1, 2, 2, 4, 4, 4]
#
#
# def calculate_mean(lst):
#     return sum(lst) / len(lst)
#
#
# def caulculate_median(lst):
#     sorted_lst = sorted(lst)
#     len_lst = len(lst)
#     mid_index = len_lst // 2
#     if len_lst % 2 == 0:
#         return (sorted_lst[mid_index - 1] + sorted_lst[mid_index]) / 2
#     else:
#         return lst[mid_index]
#
#
# def calculate_mode(lst):
#     items = {}
#     for i in lst:
#         if i in items:
#             items[i] += 1
#         else:
#             items[i] = 1
#
#     return max(items.values())
#
#
# # print(calculate_mean(numbers))
# # print(caulculate_median(numbers))
# print(calculate_mode(numbers))

## 1. Write a function called is_prime, which checks if a number is prime.
"""
To check if a number n is prime, first see if it's less than 2 — if so, it's not prime.
Otherwise, try dividing n by every number from 2 to n - 1. If any number divides it evenly, then n is not prime. If none do, then n is a prime number.
"""
# def is_prime(n):
#     if n <= 1:
#         print("not a prime number")
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#     return True
#
#
# print(is_prime(6))

##
