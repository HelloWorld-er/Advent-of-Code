galaxies = []
total_steps = 0

with open("../input/input11.txt", "r") as input_file:
    image = input_file.readlines()
    image = [list(line.strip()) for line in image]
    row_index = 0
    column_index = 0
    while row_index < len(image):
        if '#' not in image[row_index]:
            image.insert(row_index, [element for element in image[row_index]])
            row_index += 2
        else:
            row_index += 1
    while column_index < len(image[0]):
        decide = True
        for line in image:
            if line[column_index] == '#':
                decide = False
                break
        if decide:
            for line_index in range(len(image)):
                image[line_index].insert(column_index, '.')
            column_index += 2
        else:
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
    for first_galaxy_index in range(len(galaxies) - 1):
        first_galaxy = galaxies[first_galaxy_index]
        for second_galaxy_index in range(first_galaxy_index + 1, len(galaxies)):
            second_galaxy = galaxies[second_galaxy_index]
            total_steps += abs(second_galaxy[0] - first_galaxy[0]) + abs(second_galaxy[1] - first_galaxy[1])

print(total_steps)
