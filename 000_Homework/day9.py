## 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to drive")
# else:
#     years_left = 18 - age
#     if years_left == 1:
#         print("You need to wait: ", years_left, "more year to be able to drive")
#     else:
#         print("You need to wait: ", years_left, "more years to be able to drive")
#
#
# ## 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)?
## Use input(“Enter your age: ”) to get the age as input.
##You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
## and a custom text if my_age = your_age. Output:

# my_age = int(input("Enter my age: "))
# your_age = int(input("Enter your age: "))
#
# diff_years = my_age - your_age
# if my_age != your_age:
#     if my_age < your_age:
#         if abs(diff_years) == 1:
#             print("You are older than me with :", abs(diff_years), "year")
#         else:
#             print("You are older than me with: ", abs(diff_years), "years")
#     else:
#         if diff_years == 1:
#             print("I'm older than you with : ", diff_years, "year")
#         else:
#             print("I'm older than you with: ", diff_years, "years")
# else:
#     print("We have the same age")


## 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
## if a is less b return a is smaller than b, else a is equal to b. Output:
#
# a, b = input("Enter two numbers(with space between them): ").split()
# if a > b:
#     print(a, "is greater than", b)
# elif a < b:
#     print(a, "is less than", b)
# else:
#     print(a, "is equal with", b)
#
# """
# 1. Write a code which gives grade to students according to theirs scores:
#
#      80-100, A
#      70-89, B
#      60-69, C
#      50-59, D
#      0-49, F
#
# """
# grade = 12
# if grade >= 80 and grade < 101:
#     print("Grade A")
# elif grade >= 70 and grade < 90:
#     print("Grade B")
# elif grade >= 60 and grade < 70:
#     print("Grade C")
# elif grade >= 50 and grade < 60:
#     print("Grade D")
# elif grade >= 0 and grade < 50:
#     print("Grade F")


# """
# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#  September, October or November, the season is Autumn.
#  December, January or February, the season is Winter.
#  March, April or May, the season is Spring
#  June, July or August, the season is Summer
#
# """
#
# month = input("Enter current month: ").lower()
# autum = ["september", "october", "november"]
# winter = ["december", "january", "february"]
# spring = ["march", "april", "may"]
# summer = ["june", "july", "august"]
#
# if month in autum:
#     print("The season is Augumn")
# elif month in winter:
#     print("The season is Winter")
# elif month in spring:
#     print("The season is Spring")
# elif month in summer:
#     print("The season is Summer")
# else:
#     print("Not a valid month")


# """
# 2. The following list contains some fruits:
#
#  fruits = ['banana', 'orange', 'mango', 'lemon']
#
#  If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#  If the fruit exists print('That fruit already exist in the list')
#
# """
#
# fruits = ["banana", "orange", "mango", "lemon"]
# fruit = ["caisa", "orange"]
# print(fruits)
#
# for f in fruit:
#     if f not in fruits:
#         print("Fruit", f, "not in the list ---> adding it")
#         fruits.append(f)
#         print("Fruit added to the list,", fruits)
#     else:
#         print("Fruit already in the list")
# print(fruits)


"""
   1. Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

     * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
     * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
     * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person
     skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
     Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
     * If the person is married and if he lives in Finland, print the information in the following format:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

"""

person = {
    "first_name": "Alex",
    "last_name": "Margarit",
    "age": 35,
    "country": "France",
    "is_marred": False,
    "skills": ["Sql", "Python", "Snowflake", "Pyspark", "Dagster"],
    "address": {"street": "Boian", "zipcode": "02210"},
}

# if "skills" in person:
#     skillz = person["skills"]
#     num_items = len(skillz)
#     mid_index = num_items // 2
#     print("I have skills:", skillz[mid_index])
#     for i in skillz:
#         if i == "Python":
#             print("Yes, I also know", i)
# else:
#     print("I don't have skills")


# if "skills" in person:
#     skillz = person["skills"]
#     skillz = set(skillz)
#     de = {"Sql", "Python"}
#     da = {"Dagster", "Pyspark"}
#     if de.issubset(skillz):
#         print("He is DE")
#     elif da.issubset(skillz):
#         print("He is a DA")
# else:
#     print("I dont have skillz")


if person["is_marred"] == True and person["country"] == "Romania":
    print(
        person["first_name"] + person["last_name"],
        "lives in ",
        person["country"],
        ". He is married",
    )
elif person["is_marred"] == True and person["country"] != "Romania":
    print(
        person["first_name"] + " " + person["last_name"],
        "lives in ",
        person["country"],
        ". Not the correct country",
    )
elif person["is_marred"] == False and person["country"] == "Romania":
    print(
        person["first_name"] + " " + person["last_name"],
        "lives in ",
        person["country"],
        ". He is NOT married",
    )
elif person["is_marred"] == False and person["country"] != "Romania":
    print(
        person["first_name"] + " " + person["last_name"],
        "is not married and does not live in the correct country",
    )
