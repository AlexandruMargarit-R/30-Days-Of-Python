# countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 4. Use for loop to print each country in the countries list.

# for country in countries:
#     print(country)
#
# # 5. Use for to print each name in the names list.
# for name in names:
#     print(name)
#
# 6. Use for to print each number in the numbers list.
# for number in numbers:
#     print(number)
#
# 1. Use map to create a new list by changing each country to uppercase in the countries list

# upper_countries = list(map(lambda x: x.upper(), countries))
# print(upper_countries)

# 1. Use map to create a new list by changing each number to its square in the numbers list
# squared = list(map(lambda x: x**2, numbers))
# print(squared)

# 1. Use map to change each name to uppercase in the names list

# lower = list(map(lambda x: x.lower(), names))
# print(lower)

# 1. Use filter to filter out countries containing 'land'.

# land = list(filter(lambda x: not "land" in x, countries))
# print(land)

# 1. Use filter to filter out countries having exactly six characters.

# six = list(filter(lambda x: len(x) != 6, countries))
# print(six)

# 1. Use filter to filter out countries containing six letters and more in the country list.

# xis = list(filter(lambda x: len(x) >= 6, countries))
# print(xis)
# 1. Use filter to filter out countries starting with an 'E'

# e = list(filter(lambda x: x.startswith("E"), countries))
# print(e)

# 1. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

# chain = list(
#     map(lambda x: x.upper(), countries).filter(lambda y: y.startswith("D"), countries)
# )
#
# print(chain)

# chain = [x.upper() for x in countries if x.upper().startswith("D")]
# print(chain)

# 1. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

# lst = [1, "hello", 3.14, "world", True]
#
#
# def get_string_lists(lst):
#     str_lst = []
#     for i in lst:
#         if type(i) is str:
#             str_lst.append(i)
#     return str_lst
#
#
# print(get_string_lists(lst))

# import os
# import sys
#
# sys.path.append("..")
#
# from data.countries import countries

#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# summed = reduce(lambda x, y: x + y, numbers)
# print(summed)

# 1. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
#
# all_minus_last = reduce(lambda x, y: x + ", " + y, countries[:-1])
# last = countries[-1]
# concated = f"{all_minus_last}, and  {last}  are north European countries"
#
# print(concated)


# 1. Declare a function called categorize_countries that returns a list of countries with some common pattern
# (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py)
# in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

# print(countries)


# filtru = lambda x: x in ""
# def categorize_countries(lst, filtru):
#     lst_new = []
#     for i in lst:
#         if filtru in i:
#             lst_new.append(i)
#     return lst_new
#
#
# print(categorize_countries(countries, "stan"))

# 1. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.


# def dictionary(lst):
#     dic = {}
#     for i in lst:
#         first_letter = i[0]
#         if not first_letter in dic:
#             dic[first_letter] = 1
#         else:
#             dic[first_letter] += 1
#     return dic
#
#
# print(dictionary(countries))


# 1. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.


# def get_first_ten_countries(lst):
#     return lst[0:10]
#
#
# print(get_first_ten_countries(countries))

# 1. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


# def get_last_ten_countries(lst):
#     return lst[-10:]
#
#
# print(get_last_ten_countries(countries))

# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# - Sort countries by name, by capital, by population
# - Sort out the ten most spoken languages by location.
# - Sort out the ten most populated countries.


import os
import sys

sys.path.append("..")

from data.countries_data import data

# print(data[1:3])
#
# newlist = sorted(data, key=lambda d: (d["name"], d["capital"], d["population"]))
# print(newlist)


# def top_10_lang(lst):
#     langs = {}
#     for i in lst:
#         for j in i["languages"]:
#             if not j in langs:
#                 langs[j] = 1
#             else:
#                 langs[j] += 1
#     sorted_list = sorted(langs.items(), key=lambda x: x[1], reverse=True)
#     return sorted_list[:10]
#
#
# print(top_10_lang(data))


def top_10_pop(lst):
    sorted_lst = sorted(lst, key=lambda x: x["population"], reverse=True)
    pop_list = []
    for i in sorted_lst:
        pop_list.append((i["name"], i["population"]))

    return pop_list[:10]


print(top_10_pop(data))
