import string

data = open("rucksack_input.txt", "r")
group = []
result = 0

alpha_dict = dict(zip(string.ascii_letters, range(1, 53)))
print(alpha_dict)

for row in data:
    if len(group) < 3:
        group.append(row[0:-1])
        #print(group)
        if len(group) >= 3:
            final_match = str(set(group[0]).intersection(group[1],group[2]))

            for i in final_match:
                if i.isalpha():
                    result = result + alpha_dict[i]
                    #print("Der Buchstabe: " + i + " hat den Wert: " + str(alpha_dict[i]))

            group = []
            final_match = ""

print(result)
data.close()
