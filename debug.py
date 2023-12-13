total = 0
symbol_format_info = []
number_format_info = []
present_list = []
pointers = []
layer = 0


def check(symbol_list, number_list, unknown_list, unknown_index):
	damaged_list = []
	decide = False
	for symbol_index in range(len(symbol_list)):
		if (symbol_list[symbol_index] == '#') or (symbol_index in unknown_index):
			if decide:
				damaged_list[-1] += 1
			else:
				decide = True
				damaged_list.append(1)
		elif decide:
			decide = False
	if damaged_list == number_list:
		return True
	return False


def recursion(index, number_index, uncertain_pointers_num, symbol_list, number_list, pointers):
	global layer
	if index >= len(pointers):
		if uncertain_pointers_num == 0 and number_index == len(number_list):
			return 1
		return 0
	print(pointers)
	print(index)
	answer = 0
	num_of_sharp = 0
	for symbol in symbol_list[pointers[index][0]: pointers[index][1] + 1]:
		if symbol == '#':
			num_of_sharp += 1
	new_pointers = [element for element in pointers]
	if num_of_sharp == 0:
		# skip
		answer += recursion(index + 1, number_index, uncertain_pointers_num + 1, symbol_list, number_list, new_pointers)
	# elif num_of_sharp == number_list[number_index]:
	# 	answer += recursion(index + 1, number_index + 1, uncertain_pointers_num)
	num = number_list[number_index]
	# split
	for start in range(pointers[index][0], pointers[index][1] + 1 - num):
		if start > 0 and symbol_list[start - 1] == '#':
			break
		if start < len(symbol_list) and symbol_list[start + 1] == '#':
			continue
		new_pointers[index][0] = start
		new_pointers.insert(index + 1, [element for element in new_pointers[index]])
		new_pointers[index][1] = start + num - 1
		new_pointers[index + 1][0] = start + num
		answer += recursion(index + 1, number_index + 1, uncertain_pointers_num - 1, symbol_list, number_list, new_pointers)
	return answer


def loop_order(symbol_list, number_list, pointers):
	# new_pointers = [element for element in pointers]
	uncertain_pointers_num = len(number_list) - len(pointers)
	return recursion(0, 0, uncertain_pointers_num, symbol_list, number_list, pointers)


with open("2023/input/input12.txt", "r") as input_file:
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
		total += loop_order(symbol_format_info[case], number_format_info[case], pointers[case])
		print()

print(total)
