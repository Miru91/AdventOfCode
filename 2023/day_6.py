i = 0

def calculate_options(time, distance):
    timing = 1
    distance = 0
    time = int(time)
    while timing < time:
        if timing == 1:
            distance = time - timing
            timing += 1
        else:
            timing += 1
            continue
        timing += 1
    return distance

with open("input6_1.txt") as file:
    data = file.read().splitlines()
    time = list(filter(None, data[0].replace("Time:","").split(" ")))
    distance = list(filter(None, data[1].replace("Distance:","").split(" ")))
    print(time)
    while i < len(time):
        print(calculate_options(time[i], distance[i]))
        i += 1