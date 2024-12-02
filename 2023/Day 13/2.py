total = 0
info = []


def compare_two_str(str_1, str_2):
	"""compare two str, decide whether two str only have one character different or not"""
	# print(str_1, str_2)
	if len(str_1) != len(str_2):
		return False
	result = sum(c1 != c2 for c1, c2 in zip(str_1, str_2))
	return result == 1


def find_vertical_line(pattern):
	vertical_index_dict = {}
	vertical_lines_dict = {}
	vertical_line_position = []
	for line_x_index in range(len(pattern[0])):
		temp_list = []
		for line_y_index in range(len(pattern)):
			temp_list.append(pattern[line_y_index][line_x_index])
		if str(temp_list) not in vertical_lines_dict:
			vertical_lines_dict[str(temp_list)] = [line_x_index]
		else:
			vertical_lines_dict[str(temp_list)].append(line_x_index)
		vertical_index_dict[line_x_index] = temp_list
	
	for line_x_index in range(len(pattern[0]) - 1):
		if vertical_index_dict[line_x_index] == vertical_index_dict[line_x_index + 1]:
			temp_list = [line_x_index - 1, line_x_index + 2]
			temp_bool = True
			temp_num = 0
			while temp_list[0] >= 0 and temp_list[1] < len(pattern[0]):
				if vertical_index_dict[temp_list[0]] != vertical_index_dict[temp_list[1]]:
					temp_bool = False
					if compare_two_str(str(vertical_index_dict[temp_list[0]]), str(vertical_index_dict[temp_list[1]])) is True:
						temp_num += 1
						temp_bool = True
				if temp_bool is False:
					break
				temp_list[0] -= 1
				temp_list[1] += 1
			if temp_bool is True and temp_num == 1:
				vertical_line_position = [line_x_index, line_x_index + 1]
				break
		elif compare_two_str(vertical_index_dict[line_x_index], vertical_index_dict[line_x_index + 1]) is True:
			temp_list = [line_x_index - 1, line_x_index + 2]
			temp_bool = True
			while temp_list[0] >= 0 and temp_list[1] < len(pattern[0]):
				if vertical_index_dict[temp_list[0]] != vertical_index_dict[temp_list[1]]:
					temp_bool = False
					break
				temp_list[0] -= 1
				temp_list[1] += 1
			if temp_bool is True:
				vertical_line_position = [line_x_index, line_x_index + 1]
				break
	# print(vertical_lines_dict)
	if vertical_line_position == []:
		return False, vertical_line_position
	return True, vertical_line_position


def find_horizontal_line(pattern):
	horizontal_index_dict = {}
	horizontal_lines_dict = {}
	horizontal_line_position = []
	for line_index in range(len(pattern)):
		horizontal_index_dict[line_index] = [_ for _ in pattern[line_index]]
		if str(horizontal_index_dict[line_index]) not in horizontal_lines_dict:
			horizontal_lines_dict[str(horizontal_index_dict[line_index])] = [line_index]
		else:
			horizontal_lines_dict[str(horizontal_index_dict[line_index])].append(line_index)
	for line_index in range(len(pattern) - 1):
		if horizontal_index_dict[line_index] == horizontal_index_dict[line_index + 1]:
			temp_list = [line_index - 1, line_index + 2]
			temp_bool = True
			temp_num = 0
			while temp_list[0] >= 0 and temp_list[1] < len(pattern):
				if horizontal_index_dict[temp_list[0]] != horizontal_index_dict[temp_list[1]]:
					temp_bool = False
					if compare_two_str(str(horizontal_index_dict[temp_list[0]]), str(horizontal_index_dict[temp_list[1]])) is True:
						temp_num += 1
						temp_bool = True
				if temp_bool is False:
					break
				temp_list[0] -= 1
				temp_list[1] += 1
			if temp_bool is True and temp_num == 1:
				horizontal_line_position = [line_index, line_index + 1]
				break
		elif compare_two_str(horizontal_index_dict[line_index], horizontal_index_dict[line_index + 1]) is True:
			temp_list = [line_index - 1, line_index + 2]
			temp_bool = True
			while temp_list[0] >= 0 and temp_list[1] < len(pattern):
				if horizontal_index_dict[temp_list[0]] != horizontal_index_dict[temp_list[1]]:
					temp_bool = False
					break
				temp_list[0] -= 1
				temp_list[1] += 1
			if temp_bool is True:
				horizontal_line_position = [line_index, line_index + 1]
				break
	# print(horizontal_lines_dict)
	if horizontal_line_position == []:
		return False, horizontal_line_position
	return True, horizontal_line_position


def find_reflection(pattern):
	result = find_horizontal_line(pattern)
	if result[0] is True:
		return 100 * (result[1][0] + 1)
	
	result = find_vertical_line(pattern)
	if result[0] is True:
		return result[1][0] + 1


with open("../input/input13.txt") as input_file:
	for line in input_file:
		if line == '\n':
			total += find_reflection(info)
			info = []
		else:
			info.append(list(line.strip()))
	if info != []:
		total += find_reflection(info)

print(total)
