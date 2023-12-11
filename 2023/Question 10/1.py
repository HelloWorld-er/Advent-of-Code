surrounding_position = [(0, -1), (1, 0), (0, 1), (-1, 0)]
connect_side = {'|': [(True, False, True, False), (0, 2)],
                '-': [(False, True, False, True), (1, 3)],
                'L': [(True, True, False, False), (0, 1)],
                'J': [(True, False, False, True), (0, 3)],
                '7': [(False, False, True, True), (2, 3)],
                'F': [(False, True, True, False), (1, 2)],
                'S': [(True, True, True, True), (0, 1, 2, 3)],
                '.': [(False, False, False, False), (-1)]}
# North, east, south, west
connect = {0: 2, 1: 3, 2: 0, 3: 1}

max_steps = -1


def decide_connect(original_index, new_index):
    global sketch, connect_side, connect
    original_pipe = sketch[original_index[1]][original_index[0]]
    new_pipe = sketch[new_index[1]][new_index[0]]
    original_sides = connect_side[original_pipe][0]
    new_sides = connect_side[new_pipe][0]
    for index in range(4):
        if original_sides[index] is True and new_sides[connect[index]] is True:
            for side in connect_side[new_pipe][1]:
                temp_x = new_index[0] + surrounding_position[side][0]
                temp_y = new_index[1] + surrounding_position[side][1]
                if temp_x == original_index[0] and temp_y == original_index[1]:
                    return True
    return False


def breadth_first_search():
    global queue_list, steps, sketch, surrounding_position, max_steps
    step = 1
    decide = False
    while len(queue_list):
        if decide:
            step += 1
            decide = False
        else:
            decide = True
        index_x = queue_list[0][0]
        index_y = queue_list[0][1]
        del queue_list[0]
        for position_x, position_y in surrounding_position:
            new_index_x = index_x + position_x
            new_index_y = index_y + position_y
            if new_index_x < 0 or new_index_x >= len(sketch[0]):
                continue
            if new_index_y < 0 or new_index_y >= len(sketch):
                continue
            if steps[new_index_y][new_index_x] == -1 and decide_connect((index_x, index_y), (new_index_x, new_index_y)):
                steps[new_index_y][new_index_x] = step
                max_steps = step
                queue_list.append((new_index_x, new_index_y))


with open("../input/input10.txt", "r") as input_file:
    sketch = input_file.readlines()
    sketch = [line.strip() for line in sketch]
    index_x = 0
    index_y = 0
    for line in sketch:
        index_x = line.find('S')
        if index_x != -1:
            break
        index_y += 1
    steps = [[-1 for pipe in range(len(line))] for line in sketch]
    steps[index_y][index_x] = 0
    queue_list = [(index_x, index_y)]
    breadth_first_search()
    for line in steps:
        print(line)

print(max_steps)
