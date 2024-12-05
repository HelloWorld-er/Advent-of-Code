with open("../input/input4.txt") as f:
    patterns = [list(tuple(i.strip())) for i in f.readlines()]
    # "XMAS"
    surrounding_positions = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    pattern = {"M", "S"}
    total_valid = 0
    for i in range(len(patterns)):
        for j in range(len(patterns[i])):
            if patterns[i][j] == "A":
                if i == 0 or i == len(patterns) - 1 or j == 0 or j == len(patterns[i]) - 1:
                    continue
                is_format = True
                if {patterns[i-1][j-1], patterns[i+1][j+1]} == pattern and {patterns[i-1][j+1], patterns[i+1][j-1]} == pattern:
                    total_valid += 1
    print(total_valid)