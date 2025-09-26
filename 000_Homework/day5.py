# ##Declare an empty list
# #
# # # lst = []
# # # lst = list()
# #
# # # Declare a list with more than 5 items and print the len
# # # lst = [1, 2, 3, 4, 5, 6]
# # # print(len(lst))
# #
# # ## Get the first item, the middle item and the last item of the list
# #
# # # print(lst[0], lst[4], lst[-1])
# #
# # ## Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# # # mixed_data_types = ["alex", 35, 185, False, "Romania"]
# #
# # ## Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# # it_companies = ["facebook", "google", "microsoft", "apple", "ibm", "oracle", "amazon"]
# # print(it_companies)
# #
# # ## Print the list after modifying one of the companies
# # print(len(it_companies))
# # it_companies[0] = "Booking"
# # print(it_companies)
# #
# # ## Add an IT company to it_companies
# # it_companies.append("Bkng")
# # print(it_companies)
# #
# # ## Add an IT company to it_companies
# # it_companies.insert(4, "Mega")
# # print(it_companies)
# #
# # ## Change one of the it_companies names to uppercase (IBM excluded!)
# # it_companies[0] = it_companies[0].upper()
# # print(it_companies)
# #
# # var = "#"
# # it_companies.append(var)
# # print(it_companies)
# #
# # ## Check if a certain company exists in the it_companies list.
# # print("lime" in it_companies)
# #
# # ## Sort the list using sort() method
# #
# # it_companies.sort(reverse=False)
# # print(it_companies)
# #
# # ## Reverse the list in descending order using reverse() method
# # it_companies.reverse()
# # print(it_companies)
# #
# # ## Slice out the first 3 companies from the list
# # # print(it_companies[0:3])
#
# ## Slice out the last 3 companies from the list
# # print(it_companies[-3:])
#
# ## Slice out the middle IT company or companies from the list
# # it_companies = [
# #     "oracle",
# #     "microsoft",
# #     "ibm",
# #     "google",
# #     "apple",
# #     "amazon",
# #     "Mega",
# #     "Bkng",
# #     "BOOKING",
# #     "#",
# # ]
# #
# # print(it_companies[3:4])
#
# # ## Remove the first IT company from the list
# # fang = [
# #     "oracle",
# #     "microsoft",
# #     "ibm",
# #     "google",
# #     "apple",
# #     "amazon",
# #     "Mega",
# #     "Bkng",
# #     "BOOKING",
# #     "#",
# # ]
# # # print(fang)
# # # fang.pop(0)
# # print(fang)
# #
# # ## Remove the middle IT company or companies from the list
# # del fang[4]
# # print(fang)
# #
# # ## Remove the last IT company from the list
# # del fang[-1]
# # print(fang)
# #
# # ## Remove all IT companies from the list
# # # fang.clear()
# # # print(fang)
# #
# # ## Destroy the IT companies list
# # # del fang
# # # print(fang)
# #
# # ## Join the following lists:
# # front_end = ["HTML", "CSS", "JS", "React", "Redux"]
# # back_end = ["Node", "Express", "MongoDB"]
# # full_stack = front_end + back_end
# # print(full_stack)
# #
# # ## After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
# #
# # new = ["Python", "SQL", "Redux"]
# # full_stack = full_stack + new
# # print(full_stack)
#
#
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#
# ages.sort()
# print(min(ages), max(ages))
# # min_age = min(ages)
# # max_age = max(ages)
# ages.append(min(ages))
# ages.append(max(ages))
# print(ages)
#
# del ages
# print("ages list deleted")
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#
# ages.sort()
# print(min(ages), max(ages))
# # min_age = min(ages)
# # max_age = max(ages)
# ages.append(min(ages))
# ages.append(max(ages))
# print(ages)
#
# import statistics as st
#
# del ages
# print("ages list deleted")
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# print(st.mean(ages))
# print(st.median(ages))
# print(max(ages) - min(ages))
#
# ## Compare the value of (min - average) and (max - average), use abs() method
# min_value = abs(min(ages) - st.mean(ages))
# print("min_value", min_value)
# max_value = abs(max(ages) - st.mean(ages))
# print("max_value", max_value)
# print(min_value == max_value)

countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombi",
    "Comoros",
    "Congo (Brazzaville)",
    "Congo",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor Timur)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia, The",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia and Montenegro",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

middle = countries[len(countries) // 2]

print(middle)


## Divide the countries list into two equal lists if it is even if not one more country for the first half.

countries_left = countries[0 : (len(countries) + 1) // 2]
countries_right = countries[(len(countries) + 1) // 2 :]
print(len(countries))
print(len(countries_left))
print(len(countries_right))


## ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
china, russia, usa, *scandic = countries
print(china, russia, usa, scandic)
