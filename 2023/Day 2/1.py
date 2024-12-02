total = 0

with open("../input/input2.txt", "r") as file_input:
	for game in file_input:
		temp_dict = {'red': 0, 'green': 0, 'blue': 0}
		temp_list = game.strip()
		temp_list = temp_list.split(':')
		temp_list = [[element] for element in temp_list]
		temp_list[-1] = temp_list[-1][0].split(';')
		temp_list[-1] = [element.split(',') for element in temp_list[-1]]
		for group in temp_list[-1]:
			for color in group:
				temp_color_list = color.split(' ')
				del temp_color_list[0]
				temp_dict[temp_color_list[-1]] = max(temp_dict[temp_color_list[-1]], int(temp_color_list[0]))
		meet_requirements = True
		for item in temp_dict.items():
			if item[0] == "red":
				if item[1] > 12:
					meet_requirements = False
					break
			elif item[0] == "green":
				if item[1] > 13:
					meet_requirements = False
					break
			elif item[0] == "blue":
				if item[1] > 14:
					meet_requirements = False
					break
		if meet_requirements is True:
			total += int(temp_list[0][0].split(' ')[-1])
print(total)