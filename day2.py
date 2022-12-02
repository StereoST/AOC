"""PART 1"""
with open("day2.txt", "r") as input_file:
    inputs = input_file.readlines()

# Score of shapes
# A Rock, B Paper, C Scissors
shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}

win_conditions = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

p1_choices = {"A": "Rock", "B": "Paper", "C": "Scissors"}
p2_choices = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

p1_score = 0
p2_score = 0

for input in inputs:
    # identify the choice
    p1_choice = p1_choices[input[0]]
    p2_choice = p2_choices[input[2]]

    # add shapre score
    p1_score += shape_score[p1_choice]
    p2_score += shape_score[p2_choice]

    if p1_choice == p2_choice:
        p1_score += 3
        p2_score += 3

    # loop through win conditions to caculate the score
    else:
        for choice, losing_choice in win_conditions.items():
            if p1_choice == choice:
                if p2_choice == losing_choice:
                    p1_score += 6
                else:
                    p2_score += 6

print(p1_score)
print(p2_score)

"""PART 2"""
outcomes = {"X": "Lose", "Y": "Draw", "Z": "Win"}

p1_score = 0
p2_score = 0

for input in inputs:
    # identify the choice
    p1_choice = p1_choices[input[0]]
    desired_outcome = outcomes[input[2]]

    # what to choose for the desired outcome
    if desired_outcome == "Lose":
        p2_choice = win_conditions[p1_choice]
    elif desired_outcome == "Win":
        losing_choice_pos = list(win_conditions.values()).index(p1_choice)
        p2_choice = list(win_conditions.keys())[losing_choice_pos]
    else:
        p2_choice = p1_choice
    
    p1_score += shape_score[p1_choice]
    p2_score += shape_score[p2_choice]

    if p1_choice == p2_choice:
        p1_score += 3
        p2_score += 3

    # loop through win conditions
    else:
        for choice, losing_choice in win_conditions.items():
            if p1_choice == choice:
                if p2_choice == losing_choice:
                    p1_score += 6
                else:
                    p2_score += 6

print(p1_score)
print(p2_score)