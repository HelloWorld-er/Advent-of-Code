galaxies = []
total_steps = 0
empty_row = {}
empty_column = {}

with open("../input/input11.txt", "r") as input_file:
    image = input_file.readlines()
    image = [list(line.strip()) for line in image]
    row_index = 0
    column_index = 0
    while row_index < len(image):
        if '#' not in image[row_index]:
            empty_row[row_index] = True
        else:
            empty_row[row_index] = False
        row_index += 1
    while column_index < len(image[0]):
        decide = True
        for line in image:
            if line[column_index] == '#':
                decide = False
                break
        if decide:
            empty_column[column_index] = True
        else:
            empty_column[column_index] = False
        column_index += 1

    for row_index in range(len(image)):
        start = 0
        while True:
            try:
                column_index = image[row_index].index('#', start)
                galaxies.append((row_index, column_index))
                start = column_index + 1
            except ValueError:
                break
    # for i in galaxies:
    # print(i)
    # print()
    for first_galaxy_index in range(len(galaxies) - 1):
        first_galaxy = galaxies[first_galaxy_index]
        for second_galaxy_index in range(first_galaxy_index + 1, len(galaxies)):
            second_galaxy = galaxies[second_galaxy_index]
            empty_row_num = 0
            empty_column_num = 0
            min_galaxy_row = min(first_galaxy[0], second_galaxy[0])
            max_galaxy_row = max(first_galaxy[0], second_galaxy[0])
            min_galaxy_column = min(first_galaxy[1], second_galaxy[1])
            max_galaxy_column = max(first_galaxy[1], second_galaxy[1])
            # print(first_galaxy, second_galaxy)
            for row in range(min_galaxy_row + 1, max_galaxy_row):
                if empty_row[row] is True:
                    empty_row_num += 1
                # print(row)
            # print()
            for column in range(min_galaxy_column + 1, max_galaxy_column):
                if empty_column[column] is True:
                    empty_column_num += 1
                # print(column)

            # print(empty_row_num, empty_column_num)
            total_steps += max_galaxy_row - min_galaxy_row + empty_row_num * (1000000 - 1)
            total_steps += max_galaxy_column - min_galaxy_column + empty_column_num * (1000000 - 1)

print(total_steps)
