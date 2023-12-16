total = 0
symbol_format_info = []
number_format_info = []
pointers = []
generated_list = []
sharp_position = []
original_sharp_position = []
group_position = []
group_dict = {}


def recursion(index, case_index, layer):
	global symbol_format_info, generated_list, sharp_position, unknown_position, group_position, group_dict, original_sharp_position
	if index == len(sharp_position) - 1:
		ans = 0
		for element_index in range(sharp_position[index][1], len(symbol_format_info[case_index])):
			if symbol_format_info[case_index][element_index] != '.':
				if element_index != sharp_position[index][1] and symbol_format_info[case_index][
					sharp_position[index][0] + element_index - sharp_position[index][1] - 1] == '#':
					break
				ans += 1
			else:
				break
		return ans
	
	answer = 0
	# print('topic', sharp_position)
	while True:
		if sharp_position[index + 1][0] - sharp_position[index][1] < 2:
			break
		if sharp_position[index][0] != 0 and symbol_format_info[case_index][sharp_position[index][0] - 1] == '#':
			break
		if sharp_position[-1][1] >= len(symbol_format_info[case_index]):
			break
		ans = 0
		for element_index in range(sharp_position[index][1], sharp_position[index + 1][0] - 1):
			if symbol_format_info[case_index][element_index] != '.':
				if element_index != sharp_position[index][1] and symbol_format_info[case_index][
					sharp_position[index][0] + element_index - sharp_position[index][1] - 1] == '#':
					break
				ans += 1
			else:
				break
		if ans == 0:
			break
		answer += ans * recursion(index + 1, case_index, layer + 1)
		temp_num = 0
		for element_index in range(sharp_position[index][0], sharp_position[index][1] + 1):
			if symbol_format_info[case_index][element_index] != '?':
				temp_num = element_index
				break
			temp_num += 1
		if temp_num >= sharp_position[index][1] - sharp_position[index][0] + 1:
			# print(layer, '-----------------')
			original_position = [i for i in sharp_position[index]]
			bool_value = False
			for top_index in range(index, len(sharp_position)):
				if top_index == index:
					element_index = sharp_position[top_index][1] + ans
				else:
					element_index = sharp_position[top_index - 1][1] + 2
				top_bool = True
				while element_index < len(symbol_format_info[case_index]):
					if symbol_format_info[case_index][element_index] != '.':
						if symbol_format_info[case_index][
							element_index - sharp_position[top_index][1] + sharp_position[top_index][0]] == '#':
							top_bool = False
							break
						temp_num = 0
						for temp_index in range(element_index, element_index - (
								sharp_position[top_index][1] - sharp_position[top_index][0] + 1), -1):
							if symbol_format_info[case_index][temp_index] == '.':
								break
							temp_num += 1
						if temp_num < sharp_position[top_index][1] - sharp_position[top_index][0] + 1:
							element_index += 1
							continue
						length = sharp_position[top_index][1] - sharp_position[top_index][0] + 1
						sharp_position[top_index][1] = element_index
						sharp_position[top_index][0] = element_index - length + 1
						break
					element_index += 1
				# print(sharp_position)
				if top_index != len(sharp_position) - 1 and sharp_position[top_index + 1][0] - \
						sharp_position[top_index][1] >= 2:
					bool_value = True
					break
				if top_bool is False:
					break
			if original_position == sharp_position[index]:
				break
			if sharp_position[-1][0] - sharp_position[-2][1] >= 2:
				bool_value = True
			if bool_value is False:
				break
		else:
			break
	
	sharp_position[index + 1][0] = original_sharp_position[index + 1][0]
	sharp_position[index + 1][1] = original_sharp_position[index + 1][1]
	
	sharp_position[index][0] = original_sharp_position[index][0]
	sharp_position[index][1] = original_sharp_position[index][1]
	return answer


def alignment(start, end, case_index):
	global sharp_position, symbol_format_info, generated_list
	# print("---------")
	# print("question", end)
	# print(symbol_format_info[case_index])
	# print(generated_list)
	
	temp_index = end
	sharp_index_start = -1
	sharp_index_end = -1
	group_index = -1
	length = -1
	while True:
		sharp_index_end = 0
		for element_index in range(temp_index - 1, -1, -1):
			if element_index >= len(generated_list):
				continue
			if generated_list[element_index] == '#':
				sharp_index_end = element_index
				break
		sharp_index_start = -1
		for element_index in range(len(sharp_position)):
			if sharp_index_end <= sharp_position[element_index][1] and sharp_index_end >= sharp_position[element_index][
				0]:
				sharp_index_start = sharp_position[element_index][0]
				sharp_index_end = sharp_position[element_index][1]
				group_index = element_index
				break
		if sharp_index_end - sharp_index_start + 1 < end - start + 1:
			temp_index = sharp_index_start
			continue
		temp_bool = True
		
		temp_num = 0
		for element_index in range(start - 1, -1, -1):
			if symbol_format_info[case_index][element_index] != '.':
				temp_num += 1
			else:
				break
		if sharp_index_end - sharp_index_start + 1 <= end - start + temp_num + 1:
			length = end - sharp_index_end
		else:
			length = start - sharp_index_start
		
		for element_index in range(sharp_index_start, sharp_index_start + length):
			if symbol_format_info[case_index][element_index] == '#':
				temp_bool = False
				break
		
		if temp_bool is False:
			temp_start = -1
			temp_end = -1
			for element_index in range(sharp_index_start + length - 1, sharp_index_start - 1, -1):
				if symbol_format_info[case_index][element_index] == '#':
					if temp_bool is False:
						temp_bool = True
						temp_end = element_index
					temp_start = element_index
				elif temp_bool is True:
					break
			
			# print(temp_start, temp_end)
			# print(sharp_index_start, sharp_index_end)
			alignment(temp_start, temp_end, case_index)
			# continue
			sharp_index_start = sharp_position[group_index][0]
			sharp_index_end = sharp_position[group_index][1]
		# print('a', sharp_index_start, sharp_index_end)
		# print(generated_list[sharp_index_start:sharp_index_end + 1])
		if sharp_index_end - sharp_index_start + 1 <= end - start + temp_num + 1:
			length = end - sharp_index_end
		else:
			length = start - sharp_index_start
		break
	# print(sharp_index_start, sharp_index_end)
	# print("length", length)
	if length >= 0:
		# print(sharp_index_start)
		for element_index in range(length):
			generated_list.insert(sharp_index_start, '.')
		temp_index = -1
		temp_group = -1
		for element_index in range(group_index, len(sharp_position)):
			sharp_position[element_index][0] += length
			sharp_position[element_index][1] += length
			temp_index = sharp_position[element_index][1] + 1
			temp_group = element_index
			if element_index != len(sharp_position) - 1 and sharp_position[element_index + 1][0] - \
					sharp_position[element_index][1] >= 2:
				break
		
		for element_index in range(length):
			if temp_index >= len(generated_list) or temp_index < 0:
				break
			del generated_list[temp_index]
		
		# print(generated_list)
		
		for element_index in range(group_index + 1, temp_group + 1):
			length = sharp_position[element_index][0] - sharp_position[element_index - 1][1]
			for temp_index in range(length - 2):
				if temp_index >= len(generated_list) or temp_index < 0:
					break
				# print(generated_list)
				del generated_list[sharp_position[element_index - 1][1] + 1]
			sharp_position[element_index][0] -= length - 2
			sharp_position[element_index][1] -= length - 2
			if element_index != len(sharp_position) - 1:
				for temp_index in range(length - 2):
					generated_list.insert(sharp_position[element_index][1] + 1, '.')
	
	# print(generated_list)
	else:
		temp_index = 0
		temp_num = 0
		# print(symbol_format_info[case_index])
		# print(generated_list)
		# print(sharp_position)
		for element_index in range(sharp_index_start - 1, -1, -1):
			if generated_list[element_index] == '.':
				temp_index = element_index
				temp_num += 1
			else:
				break
		# print(temp_index)
		# print(sharp_position)
		if temp_num >= 2:
			for element_index in range(abs(length)):
				del generated_list[temp_index]
			for element_index in range(group_index, len(sharp_position)):
				sharp_position[element_index][0] += length
				sharp_position[element_index][1] += length
		temp_group = len(sharp_position) - 1
	# print(sharp_position)
	# print(symbol_format_info[case_index])
	# print(generated_list)
	# print("----------aaaaaaaa--------------")
	# print(group_index + 1, temp_group + 1)
	# print(len(sharp_position))
	for index in range(group_index + 1, temp_group + 1):
		length = 0
		while True:
			temp_bool = True
			for element_index in range(sharp_position[index][0], sharp_position[index][1] + 1):
				if symbol_format_info[case_index][element_index] == '.':
					temp_bool = False
					break
			if temp_bool is False:
				length += 1
				generated_list.insert(sharp_position[index][0], '.')
				sharp_position[index][0] += 1
				sharp_position[index][1] += 1
			else:
				break
		temp_index = sharp_position[index][1] + 1
		for element_index in range(index + 1, len(sharp_position)):
			if sharp_position[element_index][0] - sharp_position[element_index - 1][1] >= 2:
				break
			sharp_position[element_index][0] += length
			sharp_position[element_index][1] += length
			temp_index = sharp_position[element_index][1] + 1
		# print("reach")
		# print(generated_list)
		# print(sharp_position)
		for element_index in range(length):
			# print(temp_index, len(generated_list))
			if temp_index < 0 or temp_index >= len(generated_list):
				break
			del generated_list[temp_index]


# print("hahahaaah")
# print(sharp_position)


def loop_order(case_index):
	global pointers, generated_list, number_format_info, symbol_format_info, sharp_position, group_position, group_dict, original_sharp_position
	generated_list = []
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
	
	# print(generated_list)
	
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
	# print(sharp_position)
	
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
	
	sharp_position = []
	temp_bool = False
	for element_index in range(len(generated_list)):
		if generated_list[element_index] == '#':
			if temp_bool is False:
				temp_bool = True
				sharp_position.append([element_index])
		else:
			if temp_bool is True:
				temp_bool = False
				sharp_position[-1].append(element_index - 1)
	if temp_bool is True:
		temp_bool = False
		sharp_position[-1].append(len(generated_list) - 1)
	# print(symbol_format_info[case_index])
	# print(generated_list)
	index = 0
	while index < len(symbol_format_info[case_index]):
		if symbol_format_info[case_index][index] == '#' and (
				index >= len(generated_list) or (index < len(generated_list) and generated_list[index] == '.')):
			end = 0
			for element_index in range(index, len(symbol_format_info[case_index])):
				if symbol_format_info[case_index][element_index] == '#':
					end = element_index
				else:
					break
			start = 0
			for element_index in range(index, -1, -1):
				if symbol_format_info[case_index][element_index] == '#':
					start = element_index
				else:
					break
			alignment(start, end, case_index)
		index += 1
	
	group_position = []
	temp_bool = False
	for element_index in range(len(symbol_format_info[case_index])):
		if symbol_format_info[case_index][element_index] != '.':
			if temp_bool is False:
				temp_bool = True
				group_position.append([element_index])
		else:
			if temp_bool is True:
				temp_bool = False
				group_position[-1].append(element_index - 1)
	if temp_bool is True:
		temp_bool = False
		group_position[-1].append(len(symbol_format_info[case_index]) - 1)
	
	group_dict = {}
	
	for index in range(len(sharp_position)):
		for element_index in range(len(group_position)):
			if sharp_position[index][0] >= group_position[element_index][0] and sharp_position[index][1] <= \
					group_position[element_index][1]:
				group_dict[index] = element_index
				break
	
	original_sharp_position = [[element for element in group] for group in sharp_position]
	
	# print()
	print(symbol_format_info[case_index])
	print(generated_list)
	print(group_position)
	print(group_dict)
	# print(sharp_position)
	# print(len(symbol_format_info[case_index]))
	# print()
	
	# return 0
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
		print(case)
# print(case)
# print(total - a)
# print()
# print()

print(total)