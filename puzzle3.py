# puzzle3.py: Python script that accepts a list of integers and calculates the length and the fifth
# element. Return true if the lenth of the list is 8 and the fifth element occurs thrice in the said list

#Author: Stephen Isiuwe
# Date: 25/5/2023

def check_list(lst):
    
    length = len(lst)
    fifth_element = None

    if length == 8:
        fifth_element = lst[4]

    if fifth_element is not None and lst.count(fifth_element) == 3:
        return True
    
    return False

input_list = [1, 2, 3, 4, 5, 5, 5, 6]
result = check_list(input_list)
print(result)