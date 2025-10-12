## 1. Writ a function which generates a six digit/character random_user_id.

"""
print(random_user
'1ee33d'
"""

import random
import string

# def random_user_id(n):
#     chars = string.ascii_letters
#     digits = string.digits
#     combined = chars + digits
#     randomised = random.choices(combined, k=n)
#     user_id = "".join(randomised)
#     return user_id
#
#
# print(random_user_id(6))
#
## 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
"""

# lenght, number = map(
#     int, input("Insert number of charachters and how many do you need:").split()
# )
# # print(lenght, number)
#
# user_full = random.choices(string.digits + string.ascii_letters, k=lenght)
# full_username = "".join(user_full)


# def user_id_gen_by_user():
#     lenght, number = input(
#         "Insert number of charachters and how many do you need:"
#     ).split()
#     if not (lenght.isdigit() and number.isdigit()):
#         print("Integers only")
#         return
#     len_int = int(lenght)
#     num_int = int(number)
#
#     user_full = random.choices(string.digits + string.ascii_letters, k=len_int)
#     full_username = "".join(user_full)
#
#     for i in range(0, num_int - 1):
#         print("".join(random.choices(full_username, k=len_int)), end=" ")
#     return full_username
#
#
# print(user_id_gen_by_user())


## 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
"""
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
"""


# def rgb_color_gen():
#     numbers = []
#     for i in range(3):
#         i = random.randint(0, 255)
#         numbers.append(i)
#     return f"rgb{tuple(numbers)}"
#
#
# print(rgb_color_gen())

## Create a function called list_of_hexa_colors that generates and returns an array containing hexadecimal color codes.
##Each color code should follow the standard format of a hash symbol (#) followed by exactly six hexadecimal characters.
##The hexadecimal system uses 16 different symbols: the digits 0 through 9, plus the letters a through f.
"""
['#a3c2f1', '#ff5733', '#1a2b3c', '#e8d4a0', '#0f9bd6']
"""


# hexadecimals = string.ascii_letters
# hex_deci = list(hexadecimals[0:10])
# print(hex_deci)
#
# def list_of_hexa_colors(n):
#     decimals = list(string.ascii_lowercase[0:6])
#     digits = list(string.digits)
#     combined = decimals + digits
#     concat = "".join(combined)
#     list_of_items = []
#     combined = []
#     hashed = []
#     for i in range(n):
#         i = random.choices(concat, k=6)
#         list_of_items.append(i)
#     for j in list_of_items:
#         a = "".join(j)
#         combined.append(a)
#     for item in combined:
#         item = "#" + item
#         hashed.append(item)
#
#     return hashed
#
#
# print(list_of_hexa_colors(9))

##1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.


# def list_of_rgb_colors(n):
#     rgb_list = []
#
#     for _ in range(n):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#
#         formatted = f"rgb({r}, {g}, {b})"
#         rgb_list.append(formatted)
#
#     return rgb_list
#
#
# print(list_of_rgb_colors(3))


## Create a function called generate_passwords that produces and returns an array containing randomly generated passwords.
# Each password should be exactly 8 characters long and must include a mix of uppercase letters, lowercase letters, and digits.
# The function should be flexible enough to generate any number of passwords as specified by the input parameter.


# def generate_password(n):
#     upper = string.ascii_uppercase
#     lower = string.ascii_lowercase
#     digits = string.digits
#     all_digits = upper + lower + digits
#     mandatory_cases = []
#
#     for _ in range(n):
#         u = random.choice(upper)
#         l = random.choice(lower)
#         d = random.choice(digits)
#         rem = random.choices(all_digits, k=5)
#         mandatory = [u, l, d] + rem
#         random.shuffle(mandatory)
#         formatted_list = "".join(mandatory)
#         mandatory_cases.append(formatted_list)
#
#     return mandatory_cases
#
#
# print(generate_password(4))

##1. Write a function generate_colors which can generate any number of hexa or rgb colors.
"""
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""


# def generate_colors(rgbhex, n):
#     """
#     1. import random
#     2. import string
#     3. hexa = 6 characters
#     4. rgb = list of 3 random numbers up to 255
#     5. based on the 1st function argument, generate different output
#     """
#     letters = string.ascii_lowercase[0:6]
#     digits = string.digits
#     combined = letters + digits
#     hexa = []
#     rgb = []
#
#     if rgbhex == "hexa":
#         for _ in range(n):
#             l = random.choice(letters)
#             d = random.choice(digits)
#             b = random.choices(combined, k=4)
#             e = "".join(b)
#             rgb = [l + d] + [e]
#             joined = "".join(rgb)
#             hexa.append(f"#{joined}")
#         return hexa
#     elif rgbhex == "rgb":
#         for _ in range(n):
#             r = random.randint(0, 255)
#             g = random.randint(0, 255)
#             b = random.randint(0, 255)
#             rgb_lst = f"rgb({r}, {g}, {b})"
#             rgb.append(rgb_lst)
#         return rgb
#     else:
#         return "Chose type hexa or rgb"
#
#
# print(generate_colors("rgb", 3))


## 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list


# def shuffle_list(a):
#     random.shuffle(a)
#     return a
#
#
# lst = [1, 2, 3, "t"]
#
# # print(random.shuffle(lst))
# print(shuffle_list(lst))

## 1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


# def unique_numbers():
#     numbers = set()
#     while len(numbers) < 7:
#         numbers.add(random.randint(0, 9))
#     return list(numbers)
#
#
# print(unique_numbers())
