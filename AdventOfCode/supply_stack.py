data = open("supply_stack_input_1.txt", "r")
order = open("supply_stack_input_2.txt", "r")

count = 0

for row in data:
    count = count + 1
    globals()[f"stack_{count}"] = row

print(stack_1)

data.close()
order.close()
