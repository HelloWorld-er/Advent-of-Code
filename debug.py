total = 0
symbol_format_info = []
number_format_info = []
present_list = []
pointers = []
generated_list = []
sharp_position = []


def check(case_index):
	global generated_list, symbol_format_info
	for element_index in range(len(generated_list)):
		if generated_list[element_index] == '#':
			if symbol_format_info[case_index][element_index] == '.':
				return False
		if symbol_format_info[case_index][element_index] == '#':
			if generated_list[element_index] == '.':
				return False
	return True

def recursion(index, case_index, layer):
	answer = 0
	return answer


def loop_order(case_index):
	global pointers, generated_list, number_format_info, symbol_format_info, sharp_position
	generated_list = []
	dividing_position = []
	for index in range(len(number_format_info[case_index])):
		length = number_format_info[case_index][index]
		for element in range(length):
			generated_list.append('#')
		if index < len(number_format_info[case_index]) - 1:
			generated_list.append('.')
	
	index = 0
	while index < len(symbol_format_info[case_index]):
		if symbol_format_info[case_index][index] == '?':
			break
		if symbol_format_info[case_index][index] != generated_list[index]:
			del symbol_format_info[case_index][index]
		else:
			index += 1
	length = len(symbol_format_info[case_index]) - len(generated_list)
	index = len(symbol_format_info[case_index]) - 1
	while index >= 0:
		if symbol_format_info[case_index][index] == '?':
			break
		if symbol_format_info[case_index][index] != generated_list[index - length]:
			del symbol_format_info[case_index][index]
			length -= 1
		index -= 1
	
	print(generated_list)
	
	# Use a list store each group's range
	sharp_position = []
	temp_bool = False
	for index in range(len(symbol_format_info[case_index])):
		if symbol_format_info[case_index][index] != '.':
			if temp_bool is False:
				temp_bool = True
				sharp_position.append([index])
		else:
			if temp_bool is True:
				temp_bool = False
				sharp_position[-1].append(index - 1)
	if temp_bool is True:
		temp_bool = False
		sharp_position[-1].append(len(symbol_format_info[case_index]) - 1)
	print(sharp_position)
	
	index = 0
	layer = 0
	group_index = 0
	while index < len(generated_list):
		if generated_list[index] == '#':
			length = 0
			element_index = index
			while element_index < len(symbol_format_info[case_index]):
				if element_index + number_format_info[case_index][layer] - 1 > sharp_position[group_index][1]:
					group_index += 1
					element_index = sharp_position[group_index][0]
					continue
				if symbol_format_info[case_index][element_index] != '.':
					length = element_index - index
					break
				element_index += 1
			for element in range(length):
				generated_list.insert(index, '.')
			index += length + number_format_info[case_index][layer] - 1
			layer += 1
		index += 1
	
	# Focus on symbol_format_info, change generated_list
	
	print(symbol_format_info[case_index])
	print(generated_list)
	
	return recursion(0, case_index, 0)


with (open("2023/input/input12.txt", "r") as input_file):
	for line in input_file:
		temp = line.strip().split(' ')
		symbol_format_info.append(list(temp[0]))
		number_format_info.append([int(element) for element in temp[1].split(',')])
	
	for case in range(len(symbol_format_info)):
		decide = False
		pointers.append([])
		for element_index in range(len(symbol_format_info[case])):
			element = symbol_format_info[case][element_index]
			if element == '?' or element == '#':
				if decide is False:
					pointers[-1].append([element_index])
					decide = True
			else:
				if decide is True:
					pointers[-1][-1].append(element_index - 1)
					decide = False
		if decide:
			pointers[-1][-1].append(len(symbol_format_info[case]) - 1)
	for case in range(len(symbol_format_info)):
		total += loop_order(case)
		print(case)

print(total)