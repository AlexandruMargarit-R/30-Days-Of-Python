# =====EASY=====
""" "
Difficulty: Easy

Concepts Used:

Day 5: Lists (List iteration)

Day 8: Dictionaries (Accessing values)

Day 9: Conditionals (if statement)

Day 11: Functions

Day 13: List Comprehension (Optional)

Challenge: Write a function filter_by_category that takes a list of product dictionaries. The function should return a new list containing only the products that belong to the 'fruit' category.

Input:
"""

products = [
    {"name": "apple", "category": "fruit", "price": 0.5},
    {"name": "bread", "category": "bakery", "price": 2.0},
    {"name": "banana", "category": "fruit", "price": 0.3},
    {"name": "milk", "category": "dairy", "price": 1.5},
]

# Expected Output:
# [{'name': 'apple', 'category': 'fruit', 'price': 0.5}, {'name': 'banana', 'category': 'fruit', 'price': 0.3}]


def filter_by_category(products):
    new_list = []
    for product in products:
        if product["category"] == "fruit":
            new_list.append(product)
    return new_list


# print(filter_by_category(products))

# ====MEDIUM=====
""""
Concepts Used:

Day 4: Strings (.split(), .strip())

Day 10: Loops (for loop)

Day 8: Dictionaries (Aggregation, checking existence)

Day 17: Exception Handling (try...except for type conversion)

Day 19: File Handling (reading a multiline string)

Challenge: You are given a multiline string simulating a log file (system.log). Write a function parse_log_warnings that reads this string line by line.
The function should extract the message from any line that starts with "WARNING" and return a new list of just those warning messages.

Input:
"""
log_data = """
INFO: System startup complete.
DEBUG: Connecting to database...
WARNING: CPU temperature high.
INFO: User 'admin' logged in.
ERROR: Failed to fetch data.
WARNING: Low disk space.
"""
# Expected output:

# ['CPU temperature high.', 'Low disk space.']
# import re
#
# pattern = r"A-Z:"

# log_datax = log_data.splitlines()
# # print(log_datax)
#
#
# def parse_log_warnings(log_datax, string: str):
#     warnings = []
#     warnings_clean = []
#     for item in log_datax:
#         if string in item:
#             warnings.append(item)
#     for i in warnings:
#         warnings_clean.append(i.lstrip(f"{string}: "))
#     return warnings_clean
#
#
# print(parse_log_warnings(log_datax, "INFO"))

lista_goala = []

for line in log_data.splitlines():
    if ":" in line:
        level, message = line.split(":", -1)
        lista_goala.append({"level": level.strip(), "message": message.strip()})

print(lista_goala[0]["level"])
print(lista_goala[0]["message"])

list_level = []
list_message = []
for item in lista_goala:
    list_level.append(item["level"])
    list_message.append(item["message"])

warning = []

for message in lista_goala:
    if message["level"] == "WARNING":
        warning.append(message["message"])

print(warning)


log = "WARNING: RAW data"
print("lstrip way:", log.lstrip("WARNING: "))
# Output: 'AW data' (because 'R' and ' ' were also in the set)

# Output: 'RAW data' (Correct!)
print("removeprefix way:", log.removeprefix("WARNING: "))

log = log.lstrip("WARNING: ")
print(log)
