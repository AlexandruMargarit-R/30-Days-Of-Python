# Difficulty: Medium
# Concepts Used:
# Day 18 (Regular Expressions): Using re.findall to find a pattern.
# Day 11 (Functions): Defining a function that takes a string.
# Day 7 (Sets): Using a set to get unique items (or a loop and if not in check).
# Challenge: You have a web server access log as a multi-line string. Write a function extract_ip_addresses(log_data) that takes the log data string as input and returns a list of all unique IP addresses found.
# Input:

log_data = """
192.168.1.1 - - [29/Oct/2025:10:30:01 +0000] "GET /home HTTP/1.1" 200 1543
10.0.0.1 - - [29/Oct/2025:10:30:02 +0000] "POST /login HTTP/1.1" 200 122
192.168.1.1 - - [29/Oct/2025:10:30:03 +0000] "GET /dashboard HTTP/1.1" 200 5678
172.16.0.5 - - [29/Oct/2025:10:30:05 +0000] "GET /static/style.css HTTP/1.1" 200 890
10.0.0.1 - - [29/Oct/2025:10:30:06 +0000] "GET /logout HTTP/1.1" 200 102
"""

# Expected Output: (Note: The order of IPs in the list does not matter)
["192.168.1.1", "10.0.0.1", "172.16.0.5"]

import re


def extract_ip_addresses(log_data):
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    return re.findall(pattern, log_data)


print(list(set(extract_ip_addresses(log_data))))
