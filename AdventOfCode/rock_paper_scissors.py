data = open('rock_paper_scissors_input.txt', 'r')
result = 0
match = []
# A = Rock 1
# B = Paper 2
# C = Scissor 3

# X = lose
# Y = draw
# Z = win

# Win = 6
# Draw = 3
# Lose = 0

for row in data:
    for i in row:
        if i != " " and i != "\n":
            match.append(i)
        elif i == "\n":
            if match [1] == "X":  #Lose
                if match[0] == "A":
                    result = result + 3
                elif match[0] == "B":
                    result = result + 1
                elif match[0] == "C":
                    result = result + 2
            elif match[1] == "Y": #Draw
                result = result + 3
                if match[0] == "C":
                    result = result + 3
                elif match[0] == "A":
                    result = result + 1
                elif match[0] == "B":
                    result = result + 2
            elif match[1] == "Z": #Win
                result = result + 6
                if match[0] == "B":
                    result = result + 3
                elif match[0] == "C":
                    result = result + 1
                elif match[0] == "A":
                    result = result + 2

            match = []

print(result)
