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
	global symbol_format_info, generated_list, sharp_position, group_position, group_dict, original_sharp_position
	
	answer = 0
	temp_index = -1
	while True:
		if index != len(sharp_position) - 1 and sharp_position[index + 1][0] - sharp_position[index][1] < 2:
			break
		if sharp_position[index][0] != 0 and symbol_format_info[case_index][sharp_position[index][0] - 1] == '#':
			break
		if sharp_position[-1][1] >= len(symbol_format_info[case_index]):
			break
		# print(layer, sharp_position)
		ans = 0
		if index != len(sharp_position) - 1:
			temp_num = min(group_position[group_dict[index]][1] + 1, sharp_position[index + 1][0] - 1)
			end = min(group_position[group_dict[index]][1] + 1, sharp_position[index + 1][0] - 1)
		else:
			temp_num = min(group_position[group_dict[index]][1] + 1, len(symbol_format_info[case_index]))
			end = min(group_position[group_dict[index]][1] + 1, len(symbol_format_info[case_index]))
		
		for element_index in range(sharp_position[index][1], end):
			if symbol_format_info[case_index][element_index] != '.':
				if element_index != sharp_position[index][1] and symbol_format_info[case_index][
					sharp_position[index][0] + element_index - sharp_position[index][1] - 1] == '#':
					break
				ans += 1
			else:
				temp_num = element_index
				break
		
		if ans == 0:
			break
		
		original_list = []
		for element_index in range(index + 1, len(sharp_position)):
			original_list.append([i for i in sharp_position[element_index]])
		
		original_dict = {}
		for element_index in range(index + 1, len(sharp_position)):
			original_dict[element_index] = group_dict[element_index]
		
		if index != len(sharp_position) - 1:
			answer += ans * recursion(index + 1, case_index, layer + 1)
		else:
			answer += ans
		
		# if layer == len(sharp_position) - 1:
		# 	print(sharp_position, ans)
		
		if temp_num != end or end >= len(symbol_format_info[case_index]):
			break
		
		for element_index in range(index + 1, len(sharp_position)):
			sharp_position[element_index][0] = original_list[element_index - index - 1][0]
			sharp_position[element_index][1] = original_list[element_index - index - 1][1]
		
		for element_index in range(index + 1, len(sharp_position)):
			group_dict[element_index] = original_dict[element_index]
		
		temp_bool = True
		if symbol_format_info[case_index][temp_num] == '?':
			for element_index in range(index, len(sharp_position)):
				if symbol_format_info[case_index][sharp_position[element_index][0]] == '#':
					temp_bool = False
					break
				if element_index == index:
					length = sharp_position[element_index][1] - sharp_position[element_index][0] + 1
					sharp_position[element_index][1] = temp_num
					sharp_position[element_index][0] = sharp_position[element_index][1] - length + 1
				else:
					sharp_position[element_index][0] += 1
					sharp_position[element_index][1] += 1
				if element_index != len(sharp_position) - 1 and sharp_position[element_index + 1][0] - \
						sharp_position[element_index][1] >= 2:
					break
		else:
			# print(group_dict, layer)
			# print(symbol_format_info[case_index])
			# print(generated_list)
			# print(index)
			temp_bool = True
			temp_index = len(sharp_position) - 1
			for element_index in range(index, len(sharp_position)):
				# print(group_dict)
				# print(sharp_position)
				length = sharp_position[element_index][1] - sharp_position[element_index][0] + 1
				if element_index != index:
					if sharp_position[element_index - 1][1] + 1 + length <= \
							group_position[group_dict[element_index - 1]][1]:
						bool_value = True
						while symbol_format_info[case_index][sharp_position[element_index - 1][1] + 1] == '#':
							if sharp_position[element_index - 1][1] + 1 + length > \
									group_position[group_dict[element_index - 1]][1]:
								bool_value = False
								temp_bool = False
								break
							if symbol_format_info[case_index][sharp_position[element_index - 1][0]] == '#':
								bool_value = False
								break
							sharp_position[element_index - 1][0] += 1
							sharp_position[element_index - 1][1] += 1
						
						if temp_bool is False:
							break
						
						if bool_value is True:
							sharp_position[element_index][0] = sharp_position[element_index - 1][1] + 2
							sharp_position[element_index][1] = sharp_position[element_index][0] + length - 1
							group_dict[element_index] = group_dict[element_index - 1]
							if element_index != len(sharp_position) - 1 and sharp_position[element_index + 1][0] - \
									sharp_position[element_index][1] >= 2:
								temp_index = element_index
								break
							continue
				# print(group_dict)
				temp = group_dict[element_index]
				temp_index = -1
				while True:
					if temp == len(group_position) - 1:
						temp_bool = False
						break
					# print(temp)
					if length > group_position[temp + 1][1] - group_position[temp + 1][0] + 1:
						temp += 1
					else:
						temp_index = temp + 1
						break
				if temp_bool is False:
					break
				if temp_index == -1:
					temp_bool = False
					break
				
				sharp_position[element_index][0] = group_position[temp_index][0]
				sharp_position[element_index][1] = sharp_position[element_index][0] + length - 1
				group_dict[element_index] = temp_index
				if element_index != len(sharp_position) - 1 and sharp_position[element_index + 1][0] - \
						sharp_position[element_index][1] >= 2:
					temp_index = element_index
					break
			for element_index in range(index, temp_index + 1):
				if element_index < len(sharp_position) - 1:
					if group_dict[element_index + 1] < group_dict[element_index]:
						temp_bool = False
						break
					for temp in range(sharp_position[element_index][1] + 1, sharp_position[element_index + 1][0]):
						if symbol_format_info[case_index][temp] == '#':
							temp_bool = False
							break
					if temp_bool is False:
						break
			# print(group_dict, temp_bool)
		# print(sharp_position)
		if temp_bool is False:
			break
	
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
			# print(sharp_index_start, sharp_index_end, temp_num, length)
			for element_index in range(sharp_index_start + length - 1, sharp_index_start - 1, -1):
				if symbol_format_info[case_index][element_index] == '#':
					if temp_bool is False:
						temp_bool = True
						temp_end = element_index
					temp_start = element_index
				elif temp_bool is True:
					break
			# print(temp_start, temp_end)
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
		pass
	# temp_index = 0
	# temp_num = 0
	#
	# for element_index in range(sharp_index_start - 1, -1, -1):
	# 	if generated_list[element_index] == '.':
	# 		temp_index = element_index
	# 		temp_num += 1
	# 	else:
	# 		break
	#
	# if temp_num >= 2:
	# 	for element_index in range(abs(length)):
	# 		del generated_list[temp_index]
	# 	for element_index in range(group_index, len(sharp_position)):
	# 		sharp_position[element_index][0] += length
	# 		sharp_position[element_index][1] += length
	# temp_group = len(sharp_position) - 1
	# group_index + 1, temp_group + 1
	# print("back")
	# print(symbol_format_info[case_index])
	# print(generated_list)
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
		
		# print(generated_list)
		# print(sharp_position)
		
		for element_index in range(length):
			# print(temp_index, len(generated_list))
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


# print(generated_list)


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
	
	# index = 0
	# layer = 0
	# group_index = 0
	# while index < len(generated_list):
	# 	if generated_list[index] == '#':
	# 		length = 0
	# 		element_index = index
	# 		while element_index < len(symbol_format_info[case_index]):
	# 			if element_index + number_format_info[case_index][layer] - 1 > sharp_position[group_index][1]:
	# 				group_index += 1
	# 				element_index = sharp_position[group_index][0]
	# 				continue
	# 			if symbol_format_info[case_index][element_index] != '.':
	# 				length = element_index - index
	# 				break
	# 			element_index += 1
	# 		for element in range(length):
	# 			generated_list.insert(index, '.')
	# 		index += length + number_format_info[case_index][layer] - 1
	# 		layer += 1
	# 	index += 1
	
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
		
		# print(generated_list)
		# print(sharp_position)
		
		for element_index in range(length):
			# print(temp_index, len(generated_list))
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
	# print(sharp_position)
	# print(len(symbol_format_info[case_index]))
	# print()
	
	# return 0
	return recursion(0, case_index, 0)


with (open("2023/input/input12.txt", "r") as input_file):
	# for line in input_file:
		# temp = line.strip().split(' ')
		# symbol_format_info.append(list(temp[0]))
		# number_format_info.append([int(element) for element in temp[1].split(',')])
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
		a = total
		total += loop_order(case)
		print(case)
		print(total - a)
# print()
# print()

print(total)

# .??..??..??##?. 1,1,3
# 2333772