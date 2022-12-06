# Cargo crane
# Which crate will end up on each stack

from collections import defaultdict
import re
import copy

def perform_action_part_1(crates, instruction):
    find_vars = re.search("move (\d+) from (\d+) to (\d+)", instruction)
    crates_to_move_num = int(find_vars.group(1))
    src_stack_num = int(find_vars.group(2))
    dst_stack_num = int(find_vars.group(3))
    
    # Iterate over number of crates to be moved
    for _ in range(crates_to_move_num):
        # Append the last crate of source stack to the destination stack
        crates[dst_stack_num].append(crates[src_stack_num][-1])
        # Remove the last crate of source stack
        crates[src_stack_num].pop(-1)

def perform_action_part_2(crates, instruction):
    find_vars = re.search("move (\d+) from (\d+) to (\d+)", instruction)
    crates_to_move_num = int(find_vars.group(1))
    src_stack_num = int(find_vars.group(2))
    dst_stack_num = int(find_vars.group(3))
    

    # starting position of the stack
    starting_pos = len(crates[src_stack_num]) - crates_to_move_num
    # extend the stack of crates of source stack to the destination stack
    crates[dst_stack_num].extend(crates[src_stack_num][starting_pos:])
    # pop the source stack for the number of crates moved
    for _ in range(crates_to_move_num):
        crates[src_stack_num].pop(-1)

with open("day5.txt", "r") as input_file:
    inputs = input_file.read().splitlines()
    starting_crates = inputs[:8]
    instructions = inputs[10:]

crates = defaultdict(list)
# Reverse the lines so that we go bottom to top
# For each line, populate crates dictionary
for horizontal_line in reversed(starting_crates):
    # Parallel iteration of line position and stack number
    # e.g. stack 1 is line_pos 1, stack 2 is line_pos 5
    for line_pos, stack_num in zip(range(1, 36, 4), range(1, 10)):
        if horizontal_line[line_pos] != ' ':
            crates[stack_num].append(horizontal_line[line_pos])

# the variable crates look like this
# {1: ['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T'],
#  2: ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V'],
#  3: [],
#  4: ['F', 'R', 'P', 'B', 'M', 'N', 'D'],
#  5: ['H', 'V', 'R', 'P', 'T', 'B'],
#  6: ['C', 'B', 'P', 'T'],
#  7: ['B', 'J', 'R', 'P', 'L'],
#  8: ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W'],
#  9: ['P', 'R', 'D', 'H', 'F', 'J', 'B']})

# Create copies of the crates dict
crates_part_1 = copy.deepcopy(crates)
crates_part_2 = copy.deepcopy(crates)

for instruction in instructions:
    perform_action_part_1(crates_part_1, instruction)
    perform_action_part_2(crates_part_2, instruction)

print("part1")
for _, crate_list in crates_part_1.items():
    print(crate_list[-1])

print("part2")
for _, crate_list in crates_part_2.items():
    print(crate_list[-1])