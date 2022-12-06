"""PART 1 & 2"""
# Sections of camp
# Every section has a unique ID, each Elf assigned a range of IDs
# Some overlap

# Find how many pairs does one range fully contain the other
with open("day4.txt", "r") as input_file:
    section_assignments = input_file.read().splitlines()

part1_counter = 0
part2_counter = 0
for assignments in section_assignments:
    pairs = assignments.split(",")
    # Expand the numbers
    first_range = set(range(int(pairs[0].split("-")[0]), int(pairs[0].split("-")[1]) + 1))
    second_range = set(range(int(pairs[1].split("-")[0]), int(pairs[1].split("-")[1]) + 1))
    expended_pairs = [first_range, second_range]

    if first_range.issubset(second_range) or second_range.issubset(first_range):
        part1_counter += 1
    if first_range.intersection(second_range) or second_range.intersection(first_range):
        part2_counter += 1
print(part1_counter)
print(part2_counter)