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
	
	answer = 0
	group = 0
	while group <= abs(uncertain_pointers_num) and number_index + group < len(number_list):
		num = [0]
		# num_total = 0
		if uncertain_pointers_num >= 0:
			for temp_index in range(number_index, number_index + group + 1):
				num.append(number_list[temp_index] - num[-1])
				# num_total += number_list[temp_index]
			# num_total -= group
		del num[0]
		positions_num = pointers[index][1] - pointers[index][0] + 1
		positions_num -= group
		if positions_num < num[-1]:
			break
		argument = 1
		temp_index = 0
		while temp_index < len(num):
			argument *= 
			
		if uncertain_pointers_num < 0:
			group -= 1
		else:
			group += 1
	return answer

def loop_order(symbol_list, number_list, pointers):
	new_pointers = [element for element in pointers]
	uncertain_pointers_num = len(number_list) - len(pointers)
	return recursion(0, 0, uncertain_pointers_num, symbol_list, number_list, new_pointers)


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

print(total)
