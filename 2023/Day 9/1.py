total = 0


def find_new_history(original_history_list):
	all_zero = True
	for each_history in original_history_list:
		if each_history != 0:
			all_zero = False
			break
	if all_zero:
		return 0
	new_list = []
	for history_index in range(0, len(original_history_list) - 1):
		new_list.append(original_history_list[history_index + 1] - original_history_list[history_index])
	return original_history_list[-1] + find_new_history(new_list)


with open("../input/input9.txt", "r") as input_file:
	for sand_history in input_file:
		sand_history_list = [int(each_history) for each_history in sand_history.strip().split(' ')]
		total += find_new_history(sand_history_list)

print(total)
