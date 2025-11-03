"""
Difficulty: Easy

Concepts Used:

Day 8 (Dictionaries): Accessing values by key.

Day 11 (Functions): Defining a function.

Day 10 (Loops): Iterating through a list (or Day 13: List Comprehension).

Challenge: You have a list of dictionaries, where each dictionary represents a product.
Write a function get_product_names(products) that takes this list as input and returns a new list containing
only the names of the products.
"""

# Input:

product_list = [
    {"id": "p1", "name": "Laptop", "price": 1200},
    {"id": "p2", "name": "Mouse", "price": 80},
    {"id": "p3", "name": "Keyboard", "price": 150},
]

# Expected Output:
["Laptop", "Mouse", "Keyboard"]


def get_product_names(lst):
    names = []
    for i in lst:
        names.append(i["name"])
    return names


print(get_product_names(product_list))
