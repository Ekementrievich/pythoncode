
import os

#createName.py: Python script to create a file 
# and write some text to it and then rename the 
# file

# Author: Stephen Isiuwe
# Date: 26-5-2023

def create_and_rename_file():
    # create a file
    file_name = "example.txt"
    with open(file_name, 'w') as file:
        file.write("This is some text")

    # Rename the file
    new_file_name = "new_example.txt"

    os.rename(file_name, new_file_name)

    return new_file_name

new_file =create_and_rename_file()
print("File renamed to:", new_file)
