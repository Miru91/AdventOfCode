import string

data = open("rucksack_input.txt", "r")
group = []
result = 0
counter = 1

alpha_dict = dict(zip(string.ascii_letters, range(1, 52)))
alpha_dict.update({"Z": 52})

for row in data:
    if len(group) < 3:
        group.append(row[0:-1])
        counter = counter + 1
    else:
        print(group)
        match_one = str(set(group[0]).intersection(group[1]))
        match_two = str(set(group[0]).intersection(group[2]))
        final_match = str(set(match_one).intersection(match_two))
        print(final_match)

        for i in final_match:
            if i.isalpha():
                result = result + alpha_dict[i]
                print("Der Buchstabe: " + i + " hat den Wert: " + str(alpha_dict[i]))

        group = []
        group.append(row[0:-1])
        counter = 0
        match_one = ""
        match_two = ""
        final_match = ""

print(result)
data.close()
