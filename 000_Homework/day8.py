## 1. Create  an empty dictionary called dog

dog = {}

## 2. Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Rex"
dog["color"] = "yellow"
dog["bread"] = "ciobanesc"
dog["legs"] = 4
dog["age"] = 10
print(dog)

## 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    "first_name": "Alex",
    "last_name": "Marga",
    "gender": "M",
    "age": 32,
    "marital_status": "Yes",
    "skills": ["Python", "SQL", "dbt"],
    "city": "Bucharest",
    "address": "Boian 81",
}
print(student)

## 4. Get the length of the student dictionary
print(len(student))

## 5. Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))

## 6. Modify the skills values by adding one or two skills
skillz = ["excel", "airflow", "dagster"]
student["skills"].extend(skillz)
print(student)

##  7. Get the dictionary keys as a list
keys = student.keys()
print(keys)

## 8. Get the dictionary values as a list
values = student.values()
print(values)

## 9. Change the dictionary to a list of tuples using _items()_ method

print(student.items())

## 10. Delete one of the items in the dictionary
student.pop("age")
print(student)

## 11. Delete one of the dictionaries
print(dog)
del dog
