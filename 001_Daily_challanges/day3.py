"""
Difficulty: Medium
Concepts Used:
Day 2: Variables and Data Types (Integers, Strings, Lists)
Day 5: Lists (Adding, removing, sorting)
Day 7: Sets (Converting list to set for unique elements)
Day 8: Dictionaries (Key-Value pairs, access, modification)
Day 9: Conditionals (If/Else for filtering)
Day 10: Loops (Iterating over lists and dictionaries)
Day 13: List Comprehension (For concise transformation)
Day 16: Date Time (If we were to parse dates, but we'll stick to basic string manipulation for time limit)
Day 19: File Handling (Simulated for input/output structure)
Challenge: Process simulated log data to calculate the total duration and the count of unique users for each distinct service name.

Input Data Structure: A list of strings, where each string represents a log entry. The format is: [Timestamp] [UserID] [ServiceName] [Duration_in_seconds].

Task:
Parse each log entry to extract the ServiceName, UserID, and Duration_in_seconds.
Aggregate the data by ServiceName.
For each service, calculate the total duration (sum of Duration_in_seconds).
For each service, count the number of unique users (UserID).
Output the results as a list of dictionaries, where each dictionary contains the ServiceName, TotalDuration, and UniqueUsers.
"""

# input
log_data = [
    "2023-10-25T08:00:00Z U100 api_service 15",
    "2023-10-25T08:01:00Z U200 data_pipeline 45",
    "2023-10-25T08:02:00Z U100 api_service 10",
    "2023-10-25T08:03:00Z U300 auth_service 30",
    "2023-10-25T08:04:00Z U200 data_pipeline 60",
    "2023-10-25T08:05:00Z U100 api_service 20",
    "2023-10-25T08:06:00Z U400 data_pipeline 30",
    "2023-10-25T08:07:00Z U300 auth_service 15",
]

# Expected output
[
    {"ServiceName": "api_service", "TotalDuration": 45, "UniqueUsers": 1},
    {"ServiceName": "data_pipeline", "TotalDuration": 135, "UniqueUsers": 2},
    {"ServiceName": "auth_service", "TotalDuration": 45, "UniqueUsers": 1},
]

test = "2023-10-25T08:00:00Z U100 api_service 15"

import re

sn = re.search(r"\b\w*_\w*\b", test)
print(sn)
spn = sn.span()
print("span is:", spn)
start, end = spn
print("start and and:", start, end)
print(test[start:end])

# print(re.match(r"[\b\w*_?\w*\b]", log_data, re.I))


def solution(log_data):
    lst = []

    for item in log_data:
        sn = re.search(r"\b\w*_\w*\b", item)
        dr = re.search(r"\d+$", item)
        usr = re.search(r"\bU\d+\b", item)

        if sn and dr and usr:
            service_name = sn.group()
            duration = dr.group()
            userid = usr.group()
            lst.append(
                {"ServiceName": service_name, "Duration": duration, "UserID": userid}
            )
    return lst


print(solution(log_data))
