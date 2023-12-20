total = 0
symbol_format_info = []
number_format_info = []
generated_list = []
sharp_sum = []
point_sum = []
positions = []
sharp_position = []
position_dict = {}


def recursion(index, start, case_index):
	global symbol_format_info, number_format_info, sharp_sum, point_sum, positions, position_dict
	answer = 0
	if position_dict[index] is False:
		position_dict[index] = True
		start = positions[index][0]
	for start_index in range(start, len(symbol_format_info[case_index])):
		end_index = start_index + number_format_info[case_index][index] - 1
		if end_index >= len(symbol_format_info[case_index]):
			break
		if start_index != 0:
			if point_sum[end_index] - point_sum[start_index - 1] > 0:
				continue
		else:
			if point_sum[end_index] > 0:
				continue
		positions[index] = [start_index, end_index]
		# print(index, positions)
		if index != 0:
			if sharp_sum[start_index - 1] - sharp_sum[positions[index - 1][1]] > 0:
				break
		else:
			if start_index != 0 and sharp_sum[start_index - 1] > 0:
				break
		if index != len(number_format_info[case_index]) - 1:
			ans = recursion(index + 1, end_index + 2, case_index)
			# if ans == 0:
			# 	break
			answer += ans
		else:
			if sharp_sum[len(symbol_format_info[case_index]) - 1] - sharp_sum[end_index] > 0:
				continue
			answer += 1
	# print(index, answer)
	return answer


def alignment(start, end, case_index):
	global sharp_position, symbol_format_info, generated_list
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
			if symbol_format_info[case_index][element_index] == '#':
				temp_num += 1
			else:
				break
		if sharp_index_end - sharp_index_start + 1 <= end - start + temp_num + 1:
			length = end - sharp_index_end
		else:
			length = start - sharp_index_start
		length = end - sharp_index_end
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
			alignment(temp_start, temp_end, case_index)
			sharp_index_start = sharp_position[group_index][0]
			sharp_index_end = sharp_position[group_index][1]
		if sharp_index_end - sharp_index_start + 1 <= end - start + temp_num + 1:
			length = end - sharp_index_end
		else:
			length = start - sharp_index_start
		length = end - sharp_index_end
		break
	if length >= 0:
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
	else:
		pass
	for index in range(len(sharp_position)):
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
		for element_index in range(length):
			# print(temp_index, len(generated_list))
			if temp_index < 0 or temp_index >= len(generated_list):
				break
			del generated_list[temp_index]
		
		if length > 0:
			for element_index in range(index, len(sharp_position) - 1):
				length = 0
				while sharp_position[element_index + 1][0] - sharp_position[element_index][1] - length > 2:
					del generated_list[sharp_position[element_index][1] + 1]
					length += 1
				for temp in range(element_index + 1, len(sharp_position)):
					sharp_position[temp][0] -= length
					sharp_position[temp][1] -= length


def loop_order(case_index):
	global symbol_format_info, number_format_info, sharp_sum, point_sum, positions, generated_list, sharp_position, position_dict
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
	
	temp_bool = False
	while temp_bool is False:
		temp_bool = True
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
				temp_bool = False
			index += 1
	
	for index in range(len(sharp_position)):
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
		
		for element_index in range(length):
			if temp_index < 0 or temp_index >= len(generated_list):
				break
			del generated_list[temp_index]
		
		if length > 0 and index != len(sharp_position) - 1:
			length = 0
			while sharp_position[index + 1][0] - sharp_position[index][1] - length > 2:
				del generated_list[sharp_position[index][1] + 1]
				length += 1
			for element_index in range(index + 1, len(sharp_position)):
				sharp_position[element_index][0] -= length
				sharp_position[element_index][1] -= length
	
	sharp_sum = []
	point_sum = []
	positions = [[i for i in _] for _ in sharp_position]
	position_dict = {_: False for _ in range(len(sharp_position))}
	for element_index in range(len(symbol_format_info[case_index])):
		sharp_sum.append(0)
		point_sum.append(0)
		if element_index != 0:
			sharp_sum[element_index] = sharp_sum[element_index - 1]
			point_sum[element_index] = point_sum[element_index - 1]
		if symbol_format_info[case_index][element_index] == '#':
			sharp_sum[element_index] += 1
		if symbol_format_info[case_index][element_index] == '.':
			point_sum[element_index] += 1
	# print(symbol_format_info[case_index])
	# print(generated_list)
	# print(number_format_info[case_index])
	# print(sharp_sum)
	# print(point_sum)
	# return 0
	return recursion(0, 0, case_index)


with (open("2023/input/input12.txt", "r") as input_file):
	# for line in input_file:
	# 	temp = line.strip().split(' ')
	# 	symbol_format_info.append(list(temp[0]))
	# 	number_format_info.append([int(element) for element in temp[1].split(',')])
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
		a = total
		total += loop_order(case)
		print(case)
		print(total - a)
	# print()
	# print()

print(total)

# ?###????????#
# . ###  ## #
