#!/usr/bin/env python3

#integer.py: pyhon script that find a list of integers
# meeting the givien conditions and returns "True", if such a list 
# exist, and "False" otherwise

# Author: Stephen Isiuwe
# 25/5/2023

def find_integer_list():
    numbers = []

    #Check numbers from 1 to 100
    for num in range(1, 101):
        count_19 = 0
        count_5 = 0

        # Count occurences of 19 and 5 in the number
        for digit in str(num):
            if digit == '1':
                count_19 += 1
            elif digit == '5':
                count_5 += 1
        # Check conditions
        if count_19 == 2 and count_5 >=3:
            numbers.append(num)

    # Return True if the list is not empty, False otherwise
    return True if numbers else False

# Test the function
result = find_integer_list()
print(result)