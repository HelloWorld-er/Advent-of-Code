total = 0
symbol_format_info = []
number_format_info = []
unknown_symbol_info = []
present_list = []


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


def looping(start, length, unknown_list, symbol_list, number_list):
	global present_list
	if len(present_list) == length:
		if check(symbol_list, number_list, unknown_list, present_list) is True:
			# print(present_list)
			return 1
		return 0
	ans = 0
	for index in range(start, len(unknown_list)):
		present_list.append(unknown_list[index])
		ans += looping(index + 1, length, unknown_list, symbol_list, number_list)
		del present_list[-1]
	return ans
	

def loop_order(symbol_list, number_list, unknown_list):
	global present_list
	damaged_num = 0
	for status in symbol_list:
		if status == '#':
			damaged_num += 1
	damaged_all_num = 0
	for element in number_list:
		damaged_all_num += element
	unknown_num = damaged_all_num - damaged_num
	arrangements = 0
	present_list = []
	return looping(0, unknown_num, unknown_list, symbol_list, number_list)
		


with open("../input/input12.txt", "r") as input_file:
	for line in input_file:
		temp = line.strip().split(' ')
		symbol_format_info.append(list(temp[0]))
		number_format_info.append([int(element) for element in temp[1].split(',')])
		unknown_symbol_info.append([])
		for symbol_index in range(len(symbol_format_info[-1])):
			if symbol_format_info[-1][symbol_index] == '?':
				unknown_symbol_info[-1].append(symbol_index)
	for case in range(len(symbol_format_info)):
		total += loop_order(symbol_format_info[case], number_format_info[case], unknown_symbol_info[case])

print(total)
