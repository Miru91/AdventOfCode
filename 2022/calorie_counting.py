data = open('calorie_counting_input.txt', 'r')
result = 0
final_list = []

for zeile in data:
    if zeile == "\n":
        result = 0
    else:
        result = result + int(zeile)

    if result != 0:
        final_list.append(result)

print(sum(sorted(final_list,reverse=True)[:3]))

data.close()
