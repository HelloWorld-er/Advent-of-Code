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
	temp_bool = True
	for first_element_index in range(len(pattern[0]) - 1):
		temp_bool = False
		for second_element_index in range(len(pattern[0])):
			temp_bool = False
			if compare_two_str(str(vertical_index_dict[first_element_index]), str(vertical_index_dict[second_element_index])) is True:
				temp_list = [first_element_index - 1, second_element_index + 1]
				


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
	
	temp_bool = True
	for first_element_index in range(len(pattern) - 1):
		temp_bool = False
		for second_element_index in range(first_element_index + 1, len(pattern)):
			temp_bool = False
			if compare_two_str(str(horizontal_index_dict[first_element_index]), str(horizontal_index_dict[second_element_index])) is True:
				temp_list = [first_element_index - 1, second_element_index + 1]
				temp_bool = True
				while temp_list[0] >= 0 and temp_list[1] < len(pattern):
					if horizontal_index_dict[temp_list[0]] != horizontal_index_dict[temp_list[1]]:
						temp_bool = False
						break
					temp_list[0] -= 1
					temp_list[1] += 1
				if temp_bool is False:
					continue
				temp_list = [first_element_index + 1, second_element_index - 1]
				while temp_list[0] <= temp_list[1]:
					if horizontal_index_dict[temp_list[0]] != horizontal_index_dict[temp_list[1]]:
						temp_bool = False
						break
					temp_list[0] += 1
					temp_list[1] -= 1
				if temp_bool is True:
					horizontal_line_position = [first_element_index, second_element_index]
					break
		if temp_bool is True:
			break
	if horizontal_line_position == []:
		return False, []
	return True, horizontal_line_position


def find_reflection(pattern):
	result = find_horizontal_line(pattern)
	if result[0] is True:
		return 100 * (result[1][0] + 1)
	print()
	result = find_vertical_line(pattern)
	if result[0] is True:
		return result[1][0] + 1
	return 0


with open("2023/input/input13.txt") as input_file:
	for line in input_file:
		if line == '\n':
			total += find_reflection(info)
			info = []
		else:
			info.append(list(line.strip()))
	if info != []:
		total += find_reflection(info)

print(total)
