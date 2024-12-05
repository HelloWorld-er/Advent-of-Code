with open("../input/input4.txt") as f:
    patterns = [list(tuple(i.strip())) for i in f.readlines()]
    # "XMAS"
    surrounding_positions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    pattern = ['X', 'M', 'A', 'S']
    total_valid = 0
    for i in range(len(patterns)):
        for j in range(len(patterns[i])):
            if patterns[i][j] == pattern[0]:
                for x_intercept, y_intercept in surrounding_positions:
                    if not (0 <= i+y_intercept*3 < len(patterns) and 0 <= j+x_intercept*3 < len(patterns[i])):
                        continue
                    is_format = True
                    temp_i = i
                    temp_j = j
                    for pattern_index in range(1, len(pattern)):
                        temp_i += y_intercept
                        temp_j += x_intercept
                        if patterns[temp_i][temp_j] != pattern[pattern_index]:
                            is_format = False
                            break
                    if is_format:
                        total_valid += 1
    print(total_valid)