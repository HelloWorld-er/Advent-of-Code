total = 0
info = []


def find_vertical_line(pattern):
	vertical_index_dict = {}
	vertical_line_position = []
	for line_x_index in range(len(pattern[0])):
		temp_list = []
		for line_y_index in range(len(pattern)):
			temp_list.append(pattern[line_y_index][line_x_index])
		vertical_index_dict[line_x_index] = temp_list
	for line_x_index in range(len(pattern[0]) - 1):
		if vertical_index_dict[line_x_index] == vertical_index_dict[line_x_index + 1]:
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
	if vertical_line_position == []:
		return False, vertical_line_position
	return True, vertical_line_position


def find_horizontal_line(pattern):
	horizontal_index_dict = {}
	horizontal_line_position = []
	for line_index in range(len(pattern)):
		horizontal_index_dict[line_index] = [_ for _ in pattern[line_index]]
	for line_index in range(len(pattern) - 1):
		if horizontal_index_dict[line_index] == horizontal_index_dict[line_index + 1]:
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
