data = open("camp_cleanup_input.txt", "r")
counter = 0

for row in data:
    pair = row.replace("\n", "").split(",")
    start_limit = int(pair[0].split("-")[0])
    end_limit = int(pair[0].split("-")[1])
    number_start = int(pair[1].split("-")[0])
    number_end = int(pair[1].split("-")[1])

    #if number_start >= start_limit and number_end <= end_limit:
    #    counter = counter + 1
    #elif start_limit >= number_start and end_limit <= number_end:
    #    counter = counter + 1

    if number_end >= start_limit and number_end <= end_limit or end_limit >= number_start and end_limit <= number_end:
        counter = counter + 1

print(counter)
data.close()
