#!/usr/bin/env python3

#integer2.py Python script that taccepts an integer and determines if it is greater than
# 4 ^ 4 (256) and congruent to 4 modulo 34

# Author: Stephen Isiuwe
# Date: 25/5/2023

def check_integer(num):
    if num > 4 ** 4 and num % 34 == 4:
        return True
    else:
        return False
    
# Accept an integer from the user
input_num = int(input("Enter an integer: "))

# Check if the input number meets the conditions
result = check_integer(input_num)

# print the result
if result:
    print("The number satisfies the conditions.")
else:
    print("The number does not satisfy the condition.")