from typing import List

## Create an empty tuple

tpl = ()
tpl2 = tuple()

## Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

bros = ("David", "Andrei")
sis = ("Raluca", "Ionela")

siblings = bros + sis
print(siblings)

## How many siblings do you have?
print(len(siblings))

family_members: List[str] = list(siblings)
family_members.extend(["Ion", "Marcela"])

print("Family members are:", family_members)
print(type(family_members))

## Unpack siblings and parents from family_members

siblings = family_members[0:3]
parents = family_members[4:]
print(siblings)
print(parents)


## Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "pear")
vegetables = ("carrot", "tomato")
animal = ("milk", "cheese")

food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

## Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

## Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid_index = len(food_stuff_lt) // 2
# print(food_stuff_lt)
print(food_stuff_lt[mid_index - 1 : mid_index])
print(mid_index)

## Slice out the first three items and the last three items from food_staff_lt list

print(food_stuff_lt[0:2] + food_stuff_lt[-3:])

## Delete the food_staff_tp tuple completely

del food_stuff_tp
print("food_stuff_tp was deleted")

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Is Estonia in nordic countries: ", "Estonia" in nordic_countries)
print("Is Iceland in nordic countries: ", "Iceland" in nordic_countries)
