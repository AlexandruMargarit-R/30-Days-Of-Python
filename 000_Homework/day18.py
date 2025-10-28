# 1. What is the most frequent word in the following paragraph?
import re

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."


replaced = str.replace(paragraph, ".", "")

split = str.split(replaced, " ")
print(split)


def counter(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


dicts = counter(split)
print(dicts)
sorts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)[0][0]
print(sorts)


# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

points = ["-3", "-4", "-5", "-1", "0", "4", "8"]
sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 - (-12)  # 20


points = [int(x) for x in points]
points = sorted(points)
print(points)
lowest = points[0]
print("Lowest:", lowest)
largest = points[-1]
print("Largest: ", largest)
distance = largest - lowest
print(distance)

# 1. Write a pattern which identifies if a string is a valid python variable
"""
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
"""


def is_valid_variable(string: str):
    if "-" in string:
        return False
    elif re.match(r"[0-9]", string):
        return False
    else:
        return True


print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("firstname"))


# 1. Clean the following text. After cleaning, count three most frequent words in the string.

sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""

# print(clean_text(sentence))
"I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher"
# print(most_frequent_words(cleaned_text))  # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]


def clean_text(string: str):
    return re.sub(r"[%|\$|@|#|&|;|\.|,|?|!]", "", string)


cleaned_text = clean_text(sentence)

cleaned_text_list = cleaned_text.split()
print(cleaned_text_list)


def most_frequent_words(lst: list):
    counter = {}
    for i in lst:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return counter


words = most_frequent_words(cleaned_text_list)

print("words:", words)
most_frequent = sorted(words.items(), key=lambda x: x[1], reverse=True)[0:3]
print(most_frequent)
