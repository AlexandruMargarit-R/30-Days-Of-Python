# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


## Find the length of the set it_companies
print(len(it_companies))

## Add 'Twitter' to it_companies

it_companies.add("Twitter")
print(it_companies)

## Insert multiple IT companies at once to the set it_companies
it_companies.update(["Booking", "BKNG"])
print(it_companies)
print(type(it_companies))

## Remove one of the companies from the set it_companies
it_companies.remove("Twitter")
print(it_companies)

## What is the difference between remove and discard
"""
We can remove an item from a set using _remove()_ method. If the item is not found _remove()_ method will raise errors, so it is good to check if the item exist in the given set. However, _discard()_ method doesn't raise any errors. Think of _discard()_ as being “if it is there, remove it, otherwise don’t bother me”.
"""

## Join A and B
c = A.union(B)
print(c)

## Find A intersection B
print("Find A intersection B:", A.intersection(B))

## Is A subset of B

print(" Is A subset of B: ", A.issubset(B))

## Are A and B disjoint sets

print("Are A and B disjoint sets: ", A.isdisjoint(B))

## Join A with B and B with A
print("UDATE A WITH B VALUES", A.union(B))
print("UPDATE B WITH A VALUES", A.union(B))


## What is the symmetric difference between A and B
print("Symmetric difference", A.symmetric_difference(B))

## Delete the sets completely
del A
del B

## Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
len_ages_set = len(ages)
len_age_list = len(age)
print(len_ages_set)
print(len_age_list)
print(len_age_list > len_ages_set)


## Explain the difference between the following data types: string, list, tuple and set
"""
string = can contain both letters and numbers. Are stored in quotes
list = can contain any type of data (int, float, bool, string). List are mutable, meaning they can be changed. Creating a list: lst = list() or lst = []
tuple = can contain any type of data (int, float, bool, string). Tuples are immutable, meaning they cannot be changed. Creating a tuple: tpl = tuple() or tpl = ()
set = can contain any type of data(int, foat, bool, string). Sets cannot contain any duplicated values and are usuaully unordered. Creating a set = set()
"""

## I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

string = "I am a teacher and I love to inspire and teach people"
split = string.split()
print(split)
set_split = set(split)
print(type(set_split), "Count unique words:", len(set_split))
