"""PART 1"""
with open("day3.txt", "r") as input_file:
    rucksacks = input_file.read().splitlines()

# 1 line = 1 rucksack
# first half = first compartment, second half = second compartment

# priority number: a - z = 1 to 26, A - Z = 27 to 52

# Find the sum of priorities of repeating items in each rucksack

# Split items in half

duplicate_items = []
sum_of_priority_score = 0
for rucksack in rucksacks:
    rucksack_size = len(rucksack) - 1
    rucksack_half_point = int(rucksack_size/2)
    split_rucksack = [rucksack[:rucksack_half_point], rucksack[rucksack_half_point:rucksack_size]]
    
    # create set of items that are duplicated
    duplicate_items_in_rucksack = set()
    for item in split_rucksack[0]:
        if item in split_rucksack[1]:
            duplicate_items_in_rucksack.add(item)
    
    # add into the overall duplicate items list
    for duplicate_item in duplicate_items_in_rucksack:
        duplicate_items.append(duplicate_item)

# sum up priority score
for item in duplicate_items:
    if item.isupper():
        sum_of_priority_score += ord(item) - 38
    else:
        sum_of_priority_score += ord(item) - 96   

print(sum_of_priority_score) 

"""PART 2"""
# Elves divided into groups of three
# Within each group, bade is the only item type carried by all three Elves
# Three lines = 1 single group
# The only item type appears in all three lines is the badge

# Split rucksacks into groups
groups = []
for i in range(0, len(rucksacks), 3):
    groups.append(rucksacks[i:(i + 3)])


badges = []
sum_of_priority_score = 0
# Within the same group
for group in groups:
    # Find the item that appears in all three rucksacks
    for item in group[0]:
        if (item in group[1]) and (item in group[2]):
            badges.append(item)
            print(item)
            break
        else:
            continue

# sum up priority score
for badge in badges:
    if badge.isupper():
        sum_of_priority_score += ord(badge) - 38
    else:
        sum_of_priority_score += ord(badge) - 96   

print(sum_of_priority_score) 