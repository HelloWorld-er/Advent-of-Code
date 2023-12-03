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
		power = 1
		for item in temp_dict.items():
			power *= item[1]
		total += power
print(total)