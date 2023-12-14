total = 0
symbol_format_info = []
number_format_info = []
present_list = []
pointers = []


def recursion(index, number_index, uncertain_pointers_num, symbol_list, number_list, layer, case_index):
	global pointers
	if index >= len(pointers[case_index]):
		if uncertain_pointers_num == 0 and number_index == len(number_list):
			# print("reach--------------------------------------------")
			return 1
		return 0
	
	answer = 0
	num_of_sharp = 0
	for symbol in symbol_list[pointers[case_index][index][0]: pointers[case_index][index][1] + 1]:
		if symbol == '#':
			num_of_sharp += 1
	if num_of_sharp == 0:
		# skip
		# print("skip-zero")
		# pointers[case_index][layer + 1] = [[element for element in item] for item in pointers[case_index][layer]]
		answer += recursion(index + 1, number_index, uncertain_pointers_num + 1, symbol_list, number_list, layer + 1,
		                    case_index)
	# print(pointers[index][1] - pointers[index][0] + 1, number_list[number_index]
	if number_index >= len(number_list):
		return answer
	if pointers[case_index][index][1] - pointers[case_index][index][0] + 1 == number_list[number_index]:
		# print("skip-full")
		# pointers[case_index][layer + 1] = [[element for element in item] for item in pointers[case_index][layer]]
		answer += recursion(index + 1, number_index + 1, uncertain_pointers_num, symbol_list, number_list, layer + 1,
		                    case_index)
	
	num = number_list[number_index]
	# split
	if pointers[case_index][index][0] > pointers[case_index][index][1] - num:
		return answer
	# print(pointers[case_index][layer][index][0], pointers[case_index][layer][index][1], num)
	for start in range(pointers[case_index][index][0], pointers[case_index][index][1] + 1):
		# print("split")
		if start + num - 1 > pointers[case_index][index][1]:
			# print("break2")
			break
		if start > 0 and start > pointers[case_index][index][0] and symbol_list[start - 1] == '#':
			# print("break2")
			break
		if start + num - 1 != pointers[case_index][index][1] and start + num < len(symbol_list) and symbol_list[
			start + num] == '#':
			# print("continue")
			continue
		# print("start", start)
		# pointers[case_index][layer + 1] = [[element for element in item] for item in pointers[case_index][layer]]
		if start + num - 1 >= pointers[case_index][index][1] - 1:
			answer += recursion(index + 1, number_index + 1, uncertain_pointers_num, symbol_list, number_list,
			                    layer + 1, case_index)
		else:
			original_start = pointers[case_index][index][0]
			original_end = pointers[case_index][index][1]
			pointers[case_index][index][0] = start
			
			pointers[case_index].insert(index + 1, [element for element in pointers[case_index][index]])
			pointers[case_index][index][1] = start + num - 1
			pointers[case_index][index + 1][0] = start + num + 1
			
			answer += recursion(index + 1, number_index + 1, uncertain_pointers_num - 1, symbol_list, number_list,
			                    layer + 1, case_index)
			
			pointers[case_index][index][0] = original_start
			pointers[case_index][index][1] = original_end
			del pointers[case_index][index + 1]
			
	return answer


def loop_order(symbol_list, number_list, case_index):
	global pointers
	uncertain_pointers_num = len(number_list) - len(pointers[case_index])
	return recursion(0, 0, uncertain_pointers_num, symbol_list, number_list, 0, case_index)


with open("../input/input12.txt", "r") as input_file:
	for line in input_file:
		temp = line.strip().split(' ')
		symbol_format_info.append(list(temp[0]))
		number_format_info.append([int(element) for element in temp[1].split(',')])
	
	for case in range(len(symbol_format_info)):
		decide = False
		pointers.append([])
		element_index = 0
		while element_index < len(symbol_format_info[case]):
			element = symbol_format_info[case][element_index]
			if element == '?' or element == '#':
				if decide is False:
					pointers[-1].append([element_index])
					decide = True
				element_index += 1
			else:
				if decide is True:
					pointers[-1][-1].append(element_index - 1)
					decide = False
				del symbol_format_info[case][element_index]
		if decide:
			pointers[-1][-1].append(len(symbol_format_info[case]) - 1)
	for case in range(len(symbol_format_info)):
		# a = total
		total += loop_order(symbol_format_info[case], number_format_info[case], case)
		# print(total - a)

print(total)