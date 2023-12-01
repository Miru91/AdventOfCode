number_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
all_numbers = []
sum = 0

def get_numbers(input):
    row_list = []
    
    row_list.append(find_number(input, True))
    row_list.append(find_number(input, False))

    return row_list

def find_number(input,first_number):
    word = ""

    if first_number == True:
        input = input
    else:
        input = reversed(input)
    
    for i in input:
        if i.isdigit():
            return int(i)
        else:
            if first_number == True:
                word = word + i
            else:
                word = i + word

            if len(word) >= 3:
                for num_str, num_value in number_dict.items():
                    if num_str in word:
                        return num_value
        
with open("input.txt") as file:
    data = file.read().splitlines()
    for row in data:
        return_value = get_numbers(row)
        all_numbers.append(int(str(return_value[0])+str(return_value[1])))

    for x in all_numbers:
        sum += x 
    
print(sum)