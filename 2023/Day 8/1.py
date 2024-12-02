step = 0

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
	index = 'AAA'
	actions_index = 0
	while True:
		if actions_index == len(actions):
			actions_index = 0
		step += 1
		index = elements[index][actions[actions_index]]
		if index == 'ZZZ':
			break
		actions_index += 1
print(step)
