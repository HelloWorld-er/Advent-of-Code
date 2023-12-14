total = 0
symbol_format_info = []
number_format_info = []
present_list = []
pointers = []
generated_list = []
dividing_position = []
min_dividing_position = []
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
	global pointers, generated_list, dividing_position, symbol_format_info, sharp_position
	# print("layer", layer)
	# print(generated_list)
	if len(generated_list) > len(symbol_format_info[case_index]):
		# print("sad - end -------------------------------")
		return 0
	if len(generated_list) == len(symbol_format_info[case_index]):
		# print("happy - end -------------------------------")
		# print(generated_list)
		if check(case_index):
			return 1
		return 0
	answer = 0
	find_sharp = False
	while index < len(generated_list):
		# print("index", index)
		if generated_list[index] == '#':
			find_sharp = True
			# print("find # !")
			for symbol_index in range(index, len(symbol_format_info[case_index])):
				# print(symbol_format_info[case_index])
				# print(layer, generated_list)
				# print(symbol_format_info[case_index], symbol_index)
				if symbol_format_info[case_index][symbol_index] == '#' or symbol_format_info[case_index][symbol_index] == '?':
					# print("symbol_index", symbol_index)
					if symbol_index + number_format_info[case_index][layer] - 1 >= len(symbol_format_info[case_index]):
						break
					length = symbol_index - index
					temp_bool = True
					for element_index in range(symbol_index, symbol_index + number_format_info[case_index][layer]):
						if symbol_format_info[case_index][element_index] == '.':
							temp_bool = False
							break
					if temp_bool is False:
						continue
					if symbol_index > 0 and symbol_format_info[case_index][symbol_index - 1] == '#':
						break
					if symbol_index + number_format_info[case_index][layer] < len(symbol_format_info[case_index]) and symbol_format_info[case_index][symbol_index + number_format_info[case_index][layer]] == '#':
						continue
					
					for element in range(length):
						generated_list.insert(index, '.')
					# print(generated_list)
					# temp = answer
					answer += recursion(index + number_format_info[case_index][layer] + length, case_index, layer + 1)
					for element in range(length):
						del generated_list[index]
					# if temp == answer:
					# 	break
			break
		index += 1
	if find_sharp is False:
		# print(layer)
		length = len(symbol_format_info[case_index]) - len(generated_list)
		for element in range(length):
			generated_list.append('.')
		answer += recursion(len(generated_list), case_index, layer + 1)
		for element in range(length):
			del generated_list[-1]
	return answer


def loop_order(case_index):
	global pointers, generated_list, number_format_info, symbol_format_info, dividing_position, min_dividing_position, sharp_position
	generated_list = []
	dividing_position = []
	for index in range(len(number_format_info[case_index])):
		length = number_format_info[case_index][index]
		for element in range(length):
			generated_list.append('#')
		if index < len(number_format_info[case_index]) - 1:
			generated_list.append('.')
	index = 0
	# print(symbol_format_info[case_index])
	# print(generated_list)
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
		
	# print(symbol_format_info[case_index])
	# print(generated_list)
	
	if generated_list[0] != '.':
		dividing_position.append(0)
	bool_value = False
	for index in range(len(generated_list)):
		if generated_list[index] == '.':
			if bool_value is False:
				bool_value = True
				dividing_position.append(index)
		else:
			if bool_value is True:
				bool_value = False
	if generated_list[-1] != '.':
		dividing_position.append(len(generated_list))
	
	sharp_position = []
	for symbol_index in range(len(symbol_format_info[case_index])):
		if symbol_format_info[case_index][symbol_index] == '#':
			sharp_position.append(True)
		else:
			sharp_position.append(False)
	
	# print(dividing_position)
	# uncertain_pointers_num = len(number_list) - len(pointers[case_index])
	return recursion(0, case_index, 0)


with (open("2023/input/input12.txt", "r") as input_file):
	for line in input_file:
		temp = line.strip().split(' ')
		symbol_format_info.append([])
		number_format_info.append([])
		for copy in range(5):
			for element in list(temp[0]):
				symbol_format_info[-1].append(element)
			if copy < 4:
				symbol_format_info[-1].append('?')
			for element in temp[1].split(','):
				number_format_info[-1].append(int(element))
	
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
		# a = total
		total += loop_order(case)
		# print(case)
		# print(total - a)
		# print()

print(total)