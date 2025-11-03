# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words
import json

with open(
    "/Users/amargarit/Developer/git_tree/30-Days-Of-Python/data/obama_speech.txt"
) as f:
    lines = f.readlines()
    f.seek(0)
    words = f.read().split()


def counting(lines):
    count_lines = len(lines)
    count_words = len(words)

    return count_words, count_lines


linez = counting(lines)
print(linez)


with open(
    "/Users/amargarit/Developer/git_tree/30-Days-Of-Python/data/michelle_obama_speech.txt"
) as m:
    linez = m.readlines()
    m.seek(0)
    wordz = m.read().split()

print("Lines:", len(linez), "Words:", len(wordz))


with open(
    "/Users/amargarit/Developer/git_tree/30-Days-Of-Python/data/donald_speech.txt"
) as m:
    linez = m.readlines()
    m.seek(0)
    wordz = m.read().split()

print("Lines:", len(linez), "Words:", len(wordz))

with open(
    "/Users/amargarit/Developer/git_tree/30-Days-Of-Python/data/melina_trump_speech.txt"
) as x:
    linex = x.readlines()
    x.seek(0)
    wordx = x.read().split()

print("Lines:", len(linex), "Words:", len(wordx))

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]


j = open(
    "/Users/amargarit/Developer/git_tree/30-Days-Of-Python/data/countries_data.json"
)

j = json.load(j)

# print(j[7])


def most_spoken_languages(j):
    langz = {}
    for i in j:
        for lang in i["languages"]:
            if lang in langz:
                langz[lang] += 1
            else:
                langz[lang] = 1
    sort = sorted(langz.items(), key=lambda x: x[1], reverse=True)
    return sort[:3]


# print(most_spoken_languages(j))


# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))
# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]


def most_populated_countries(
    filename="/Users/amargarit/Developer/git_tree/30-Days-Of-Python/data/countries_data.json",
    top=3,
):
    with open(filename) as f:
        j = json.load(f)
    lst = []
    for country in j:
        count_pop = {"country": country["name"], "population": country["population"]}
        lst.append(count_pop)

    sort = sorted(lst, key=lambda x: x["population"], reverse=True)

    return sort[:top]


print(most_populated_countries(top=3))
