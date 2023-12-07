sum = 1
i = 0
final_sum = 0

def check_numbers(win_nums, my_nums):
    counter = 0
    for number in my_nums:
        if number in win_nums:
            counter += 1
    return counter

def remove_card_num(card_row):
    count = 0
    new_row = ""
    for i in card_row:
        count += 1
        if i == ":":
            new_row = card_row[count + 1:].split(" | ")
            break
    return new_row

with open("input4.txt") as file:
    data = file.read().splitlines()
    for row in data:
        row = row.replace("Card ", "")
        new_row = remove_card_num(row)
        winning_num = new_row[0].split(" ")
        my_numbers = list(filter(None, new_row[1].split(" ")))
        hits = check_numbers(winning_num, my_numbers)
        sum = int((2**hits)/2)
        final_sum += sum
    print(final_sum)