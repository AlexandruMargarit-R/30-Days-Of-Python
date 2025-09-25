## Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

all = "Thirty " + "Days " + "Of " + "Python"
print(all)

## Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string = "Coding " + "For " + "All"
print(string)

## Declare a variable named company and assign it to an initial value "Coding For All".
company = string
print(company)
print(len(company))

## Change all the characters to uppercase letters using upper() method.

company = company.upper()
print(company)

company = company.lower()
print(company)

## Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

company = company.capitalize()
print("capitalize():", company)
company = company.title()
print("title():", company)
company = company.swapcase()
print("swapcase():", company)

## Cut(slice) out the first word of Coding For All string.
print("slice():", company[0:7])

## Check if Coding For All string contains a word Coding using the method index, find or other methods.
string = "Coding For All"
substring = "or"
print("Using find():", string.find("All"))
print("Using index():", string.index(substring))

## Replace the word coding in the string 'Coding For All' to Python.
replacer = string.replace("Coding", "Python")
print(replacer)

## Change Python for Everyone to Python for All using the replace method or other methods.
replacer = replacer.replace("All", "Everyone")
print(replacer)

## Split the string 'Coding For All' using space as the separator (split()) .

string = "Coding For All"
separator = " "
string = string.split(separator)
print(string)

## "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

faang = "Facebook, Google/ Microsoft, Apple, IBM, Oracle, Amazon"
faang = faang.split(",")
print(faang)

## What is the character at index 0 in the string Coding For All. What is the last index of the string Coding For All. What character is at index 10 in "Coding For All" string.

string = "Coding For All"
print(string[0])
print(string[-1])
print(string[10])

## Create an acronym or an abbreviation for the name 'Python For Everyone'.
text = "Python For Everyone"
acronym = "".join(w[0] for w in text.split())
print(acronym)

## Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = "Coding For All"
cfa = "".join(w[0] for w in cfa.upper().split())
print(cfa)

##Use index to determine the position of the first occurrence of C in Coding For All. Use index to determine the position of the first occurrence of F in Coding For All.
cfa = "Coding For All"
first = "C"
last = "i"
print(cfa.index(first))
print(cfa.rindex(last))

## Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent = "You cannot end a sentence with because because because is a conjunction"
first = "because"
last = "because"
print("Find() because", sent.find("because"))
print("index() first:", sent.index(first))
print("rindex() last: ", sent.rindex(last))

## Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent = "You cannot end a sentence with because because because is a conjunction"
pto = sent[:31] + sent[54:]
print(pto)

## Does ''Coding For All' start with a substring Coding?
cfa = "Coding For All"
substring = "Coding"
end = "coding"
print(cfa.startswith(substring))
print(cfa.endswith(end))

## '   Coding For All      '  , remove the left and right trailing spaces in the given string.
cfa = "   Coding For All      "
print(cfa.strip())

## Which one of the following variables return True when we use the method isidentifier():
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())

## The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
joined = "# ".join(libs)
print(joined)

## Use the new line escape sequence to separate the following sentences.
text = """
I am enjoying this challenge.\n
I just wonder what is next.
"""
print(text)

## Use a tab escape sequence to write the following lines.
text = """
Name\t      Age\t     Country\t   City\t
Asabeneh\t  250\t     Finland\t   Helsinki\t
"""
print(text)

## Use the string formatting method to display the following:
radius = 10
area = int(3.14 * radius**2)
formmated = "The area of a circle with radius {} is {} meters square".format(
    radius, area
)
print(formmated)
print(f"the area of a circle with radius {radius} is {area} meters square")

## Make the following using string formatting methods:
a = 8
b = 6

print(
    f"""
      {a} + {b} = {a+b}
      {a} - {b} = {a -b}
      {a} * {b} = {a * b}
      {a} / {b} = {a / b}
      {a} % {b} = {a % b}
      {a} // {b} = {a // b}
      {a} ** {b} = {a ** b}
      """
)
