# longestString.py: python script to find the longest
# string in a given list of strings

# Author: Stephen Isiuwe
# Date: 26-5-2023

def find_longest_string(strings):
    longest_string = ""

    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

input_list = ["apple", "banana", "pineapple", "orange"]
longest = find_longest_string(input_list)
print(longest) 