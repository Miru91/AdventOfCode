bag = {"red": 12, "green": 13, "blue": 14}
sum = 1
final_result = 0

def check_values(values):
    for key, value in bag.items():
        if key in values:
            new_n = values.replace(key, "")
            new_n = int(new_n)

            if key == "red":
                red_values.append(new_n)
            elif key == "green":
                green_values.append(new_n)
            elif key == "blue":
                blue_values.append(new_n)

with open("input2.txt") as file:
    data = file.read().splitlines()
    for d in data:
        row = d.replace("Game ", "").split(":")
        game = row[0]
        row = row.pop(1).split(";")
        result_list = []
        green_values = []
        red_values = []
        blue_values = []
        for r in row:
            new_row = r.split(",")
            for n in new_row:
                check_values(n)
        result_list.append(sorted(red_values, reverse=True)[0])
        result_list.append(sorted(green_values, reverse=True)[0])
        result_list.append(sorted(blue_values, reverse=True)[0])
        for i in result_list:
            sum *= i

        final_result += sum
        sum = 1
    print(final_result)

