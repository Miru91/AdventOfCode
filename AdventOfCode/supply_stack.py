data = open("supply_stack_input_1.txt", "r")
orders = open("supply_stack_input_2.txt", "r")
result = []
count = 0
i = 1
j = 1

for row in data:
    count = count + 1
    globals()[f"stack_{count}"] = row.replace("\n", "").split(";")

for order in orders:
    print(order)
    order = order.replace("\n", "").split(" ")
    move = int(order[1])
    von = globals()[f"stack_{int(order[3])}"]
    nach = globals()[f"stack_{int(order[5])}"]

    while i <= move:
        if len(von) > 0:
            print("von" + str(von))
            print("nach" + str(nach))
            nach.append(von[len(von)-1])
            von.pop()
            print("von afterwards" + str(von))
            print("nach afterwards" + str(nach))
        i += 1

    i = 1

while j <= count:
    if len(globals()[f"stack_{j}"]) > 0:
        print(globals()[f"stack_{j}"])
        result.append(globals()[f"stack_{j}"][-1])
    j += 1

print(result)
data.close()
orders.close()

#VPCDMSLWJ
