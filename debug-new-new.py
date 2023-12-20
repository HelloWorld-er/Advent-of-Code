total = 0

with open("2023/input/input14.txt", "r") as input_file:
	info = input_file.readlines()
	info = [list(line.strip()) for line in info]
	# for line in info:
	# 	print(line)
	# print()
	for cycle_index in range(10000):
		original_info = [[element for element in line] for line in info]
		for straight_vertical_line_index in range(len(info[0])):
			pointer = 0
			for element_index in range(len(info)):
				if info[element_index][straight_vertical_line_index] == '#':
					pointer = element_index + 1
				elif info[element_index][straight_vertical_line_index] == 'O':
					info[element_index][straight_vertical_line_index] = '.'
					info[pointer][straight_vertical_line_index] = 'O'
					pointer += 1
		# print("north")
		# for line in info:
		# 	print(line)
		# print()
		for straight_horizontal_line_index in range(len(info)):
			pointer = 0
			for element_index in range(len(info[0])):
				if info[straight_horizontal_line_index][element_index] == '#':
					pointer = element_index + 1
				elif info[straight_horizontal_line_index][element_index] == 'O':
					info[straight_horizontal_line_index][element_index] = '.'
					info[straight_horizontal_line_index][pointer] = 'O'
					pointer += 1
		# print("west")
		# for line in info:
		# 	print(line)
		# print()
		for straight_vertical_line_index in range(len(info[0])):
			pointer = len(info) - 1
			for element_index in range(len(info) - 1, -1, -1):
				if info[element_index][straight_vertical_line_index] == '#':
					pointer = element_index - 1
				elif info[element_index][straight_vertical_line_index] == 'O':
					info[element_index][straight_vertical_line_index] = '.'
					info[pointer][straight_vertical_line_index] = 'O'
					pointer -= 1
		# print("south")
		# for line in info:
		# 	print(line)
		# print()
		for straight_horizontal_line_index in range(len(info)):
			pointer = len(info[0]) - 1
			for element_index in range(len(info[0]) - 1, -1, -1):
				if info[straight_horizontal_line_index][element_index] == '#':
					pointer = element_index - 1
				elif info[straight_horizontal_line_index][element_index] == 'O':
					info[straight_horizontal_line_index][element_index] = '.'
					info[straight_horizontal_line_index][pointer] = 'O'
					pointer -= 1
		# print("east")
		# for line in info:
		# 	print(line)
		# print()
		# for line in original_info:
		# 	print(line)
		# print()
		# for line in info:
		# 	print(line)
		# print()
		if original_info == info:
			break
		print(cycle_index)
		
	length = len(info)
	for line in range(len(info)):
		num = 0
		for element in info[line]:
			if element == 'O':
				num += 1
		total += num * length
		length -= 1
	for line in info:
		print(line)
print(total)
