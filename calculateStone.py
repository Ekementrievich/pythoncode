#!/usr/bin/env python3

# calculateStone.py: python script to calculate the number of 
# stones in each pile according to given conditions

def calculate_stone_piles(n):
    piles=[]

    # Determine if the number of piles should start with an odd or even number
    # of stones 
    start_stones = n if n % 2 == 1 else n + 1

    #calculate the number of stones in each pile
    for i in range(n):
        stones=start_stones+2 *i
        piles.append(stones)
    return piles

# Accespt the number of stone piles frm the user
num_piles = int(input("Enter the number of stone piles: "))

# calculate the number of stones in each pile
stone_piles = calculate_stone_piles(num_piles)

# print the number of stones in each pile
for i, stones in enumerate(stone_piles):
    print(f"Pile {i + 1}: {stones} stones")

