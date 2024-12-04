with open("../input/input1.txt") as f:
    list1 = []
    list2 = []
    list_2_map = {}
    total_distance = 0
    for line in f:
        line = [int(i) for i in line.strip().split(" ") if i]
        list1.append(line[0])
        list2.append(line[1])
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])
    print(total_distance)