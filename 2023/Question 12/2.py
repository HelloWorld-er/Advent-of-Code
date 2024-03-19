from enum import Enum


class StringDataState(Enum):
	OPERATIONAL = '.'
	DAMAGED = '#'
	UNKNOWN = '?'


"""Dynamic Programming !!!"""
record = {}


def is_valid_condition(str_list, num_list):
	return (
			num_list[0] <= len(str_list) and StringDataState.OPERATIONAL.value not in str_list[:num_list[0]] and
			(num_list[0] == len(str_list) or str_list[num_list[0]] != StringDataState.DAMAGED.value)
	)


def get_arrangements(str_list, num_list):
	global record
	
	if not num_list:
		if StringDataState.DAMAGED.value in str_list:
			return 0
		else:
			return 1
	if not str_list:
		if not num_list:
			return 1
		else:
			return 0
	
	total = 0
	if str_list[0] in [StringDataState.UNKNOWN.value, StringDataState.OPERATIONAL.value]:
		if (str_list[1:], num_list) not in record:
			record[(str_list[1:], num_list)] = get_arrangements(str_list[1:], num_list)
		total += record[(str_list[1:], num_list)]
	if str_list[0] in [StringDataState.UNKNOWN.value, StringDataState.DAMAGED.value]:
		if is_valid_condition(str_list, num_list):
			if (str_list[num_list[0] + 1:], num_list[1:]) not in record:
				record[(str_list[num_list[0] + 1:], num_list[1:])] = get_arrangements(
					str_list[num_list[0] + 1:], num_list[1:])
			total += record[(str_list[num_list[0] + 1:], num_list[1:])]
	
	return total


with open("input.txt", "r") as input_file:
	whole_data = [_.strip() for _ in input_file.readlines()]

total = 0
for strip_data in whole_data:
	# print(strip_data)
	str_list, num_list = strip_data.split(' ')
	str_list = '?'.join([str_list] * 5)
	num_list = tuple(map(int, num_list.split(',')))
	num_list = num_list * 5
	record = {}
	total += get_arrangements(str_list, num_list)
# print(str_list, num_list)

print(total)
