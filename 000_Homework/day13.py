## 1. Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# positive = [i for i in numbers if i >= 0]
# print(positive)
#
## 2. Flatten the following list of lists of lists to a one dimensional list :
"""
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

# list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flatten = [num for row in list_of_lists for i in row for num in i]
# print(flatten)
# # flatten_for = []
# for i in list_of_lists:
#     for j in i:
#         for h in j:
#             flatten_for.append(h)
#
# print(flatten_for)
# # print(list_of_lists)

# word_lists = [["apple", "banana"], ["cat", "dog"], ["egg", "fish"]]
# # # Expected output: ['apple', 'banana', 'cat', 'dog', 'egg', 'fish']
# fruits = [l for row in word_lists for l in row]
# print(fruits)

# 3. Using list comprehension create the following list of tuples:
"""
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]

"""
# lst_tpl = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
# print(lst_tpl)

"""
[(0, 1),
 (1, 1),
 (2, 2),
 (3, 6),
 (4, 24),
 (5, 120),
 (6, 720)]
"""

# import math
#
# sad = [(a, math.factorial(a)) for a in range(7)]
# print(sad)

# 4. Flatten the following list to a new list:
"""
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

"""
# countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
#
# flatten = [
#     (i[0].upper(), i[0][:3].upper(), i[1].upper()) for lists in countries for i in lists
# ]
# print(flatten)

# fruits = [["apple", "banana"], ["cherry", "date"], ["fig", "grape"]]
# # [('APPLE', 'A'), ('BANANA', 'B'), ('CHERRY', 'C'), ...]
#
# flatten = [(i.upper(), i[0:1].upper()) for list in fruits for i in list]
# print(flatten)

# 5. Change the following list to a list of dictionaries:
"""
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]

"""
# countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
#
# dict = [{"country": i.upper(), "city": j.upper()} for lst in countries for i, j in lst]
# print(dict)

countries_info = [
    [("Finland", "Helsinki", 656_000)],
    [("Sweden", "Stockholm", 975_000)],
    [("Norway", "Oslo", 693_000)],
]

# Goal: create a list of dictionaries like:
# [{'country': 'FINLAND', 'city': 'HELSINKI', 'population': 656000}, ...]

# dict2 = [
#     {"country": i.upper(), "city": j.upper(), "population": g}
#     for lst in countries_info
#     for i, j, g in lst
# ]
# print(dict2)

# 6. Change the following list of lists to a list of concatenated strings:

names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
##    output
#  ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# full_names = [i[0] + " " + i[1] for row in names for i in row]
# print(full_names)

# 7.Assume a tax of 8% on each item.
# Write a lambda function to calculate the total price for each item including tax.
# Use map() with your lambda to apply it to the list.

# discount = 0.1
# prices = [120, 250, 400, 80]
# total_price = lambda a: a * (1 - discount)
# price = list(map(total_price, prices))
# print(price)

# quantities = [2, 5, 3, 10]
# prices = [100, 250, 400, 50]
#
# stoc = lambda a, b: a * b
# total_revenue = list(map(stoc, quantities, prices))
# print(total_revenue)

# quantities = [2, 5, 3, 10]
# prices = [100, 250, 400, 50]
# discount = 0.1
#
# price = lambda a, b: a * b * (1 - discount)
# total_rev = list(map(price, quantities, prices))
# print(total_rev)

temps_f = [32, 68, 77, 104]

print(list(map(lambda a: (a - 32) * 5 / 9, temps_f)))
