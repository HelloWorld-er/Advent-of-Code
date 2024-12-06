total = 0

with open("../input/input14.txt", "r") as input_file:
	info = input_file.readlines()
	info = [list(line.strip()) for line in info]
	for j in range(len(info[0])):
		pointer = 0
		for i in range(len(info)):
			if info[i][j] == '#':
				pointer = i + 1
			elif info[i][j] == 'O':
				info[i][j] = '.'
				info[pointer][j] = 'O'
				pointer += 1
	length = len(info)
	for line in range(len(info)):
		num = 0
		for element in info[line]:
			if element == 'O':
				num += 1
		total += num * length
		length -= 1

print(total)
