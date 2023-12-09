from math import gcd

step_for_all = 0


def calculate_lcm(numbers):
	result = numbers[0]
	for number in numbers[1:]:
		result = result * number // gcd(result, number)
	return result


with open("../input/input8.txt") as file_input:
	content = file_input.readlines()
	content = [element.strip() for element in content]
	actions = []
	line_index = 0
	while True:
		if content[line_index] != "":
			actions.extend(content[line_index])
			del content[line_index]
		else:
			del content[line_index]
			break
	actions = [0 if action == 'L' else 1 for action in actions]
	elements = {}
	keywords = [" = ", "(", ", ", ")"]
	for line in content:
		temp_list = line.split(keywords[0])
		for keyword in keywords[1:]:
			temp_list = [element.split(keyword) for element in temp_list]
			temp_list = [element for sublist in temp_list for element in sublist]
		temp_list = [element for element in temp_list if element != ""]
		elements[temp_list[0]] = (temp_list[1], temp_list[2])
	end_with_A = {}
	temp_dict = {}
	for key in elements.keys():
		if key[-1] == 'A':
			end_with_A[key] = 0
			temp_dict[key] = 0
	for origin_index in temp_dict.keys():
		index = origin_index
		step = 0
		actions_index = 0
		while True:
			if actions_index == len(actions):
				actions_index = 0
			step += 1
			index = elements[index][actions[actions_index]]
			if index[-1] == 'Z':
				break
			actions_index += 1
		end_with_A[origin_index] = step
	temp_list = [value for value in end_with_A.values()]
	step_for_all = calculate_lcm(temp_list)
	
print(step_for_all)
