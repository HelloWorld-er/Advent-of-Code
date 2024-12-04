with open("../input/input1.txt") as f:
    list_map = {}
    total_similarity = 0
    for line in f:
        line = [int(i) for i in line.strip().split(" ") if i]
        if line[0] in list_map:
            list_map[line[0]][0] += 1
        else:
            list_map[line[0]] = [1, 0]
        if line[1] in list_map:
            list_map[line[1]][1] += 1
        else:
            list_map[line[1]] = [0, 1]
    for key, value in list_map.items():
        total_similarity += key * value[0] * value[1]
    print(total_similarity)