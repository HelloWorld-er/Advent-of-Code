total = 0


def out_index(index, length):
	if index < 0 or index >= length:
		return False
	return True


def find_num(index, string_list):
	nums = []
	nums.append(int(string_list[index]))
	new_index = index
	while True:
		new_index += 1
		if new_index >= len(string_list):
			break
		try:
			nums.append(int(string_list[new_index]))
			string_list[new_index] = '.'
		except ValueError:
			break
	new_index = index
	while True:
		new_index -= 1
		if new_index < 0:
			break
		try:
			nums.insert(0, int(string_list[new_index]))
			string_list[new_index] = '.'
		except ValueError:
			break
	num = 0
	for digit in nums:
		num *= 10
		num += digit
	return num, string_list
	

surrounding_position = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

with open("../input/input3.txt", "r") as file_input:
	contents = file_input.readlines()
	for line_index in range(len(contents)):
		contents[line_index] = contents[line_index].strip()
	contents = [list(element) for element in contents]
	for line_index in range(len(contents)):
		content = contents[line_index]
		for char_index in range(len(content)):
			char = content[char_index]
			try:
				temp = int(char)
			except ValueError:
				if char != '.':
					for position_x, position_y in surrounding_position:
						position_x += char_index
						position_y += line_index
						if out_index(position_x, len(content)) is False or out_index(position_y, len(contents)) is False:
							continue
						try:
							temp = int(contents[position_y][position_x])
							num, contents[position_y] = find_num(position_x, contents[position_y])
							total += num
						except ValueError:
							pass
	
print(total)