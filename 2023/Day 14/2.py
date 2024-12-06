total = 0
rocks_list = []
rocks_dict = {}

with open("../input/input14.txt", "r") as input_file:
	info = input_file.readlines()
	info = [list(line.strip()) for line in info]
	info_spin_disc = {}
	for j in range(len(info[0])):
		pointer = 0
		for i in range(len(info)):
			if info[i][j] == '#':
				pointer = i + 1
			else:
				rocks_dict[(i, j)] = [(pointer, j)]
				info[i][j] = '.'
				info[pointer][j] = 'O'
				pointer += 1
	for i in range(len(info)):
		pointer = 0

print(total)
