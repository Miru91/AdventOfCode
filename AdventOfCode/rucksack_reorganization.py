import string

data = open("rucksack_input.txt", "r")
half_one = []
half_two = []
result = 0
counter = 1

alpha_dict = dict(zip(string.ascii_letters, range(1, 52)))
alpha_dict.update({"Z": 52})

for row in data:
    first_half = slice(0, len(row)//2)
    second_half = slice(len(row)//2, len(row))

    #print("Complete String: " + row)
    #print("First Half: " + row[first_half])
    #print("Second Half: " + row[second_half])

    for i in row[first_half]:
        half_one.append(i)

    for i in row[second_half]:
        if i != "\n":
            half_two.append(i)

    matched_digit = str(set(half_one).intersection(half_two))[2]
    #print("Value of " + matched_digit + " is: " + str(alpha_dict[matched_digit]))

    result = result + alpha_dict[matched_digit]

    counter = counter + 1

    matched_digit = ""
    half_one = []
    half_two = []

print("Result is: " + str(result))

data.close()
