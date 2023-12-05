seeds = []

with open("../input/input5.txt", "r") as file_input:
	content = file_input.readlines()
	content = [each_line.strip() for each_line in content]
	temp = []
	new_list = []
	for each_line in content:
		if each_line == '':
			new_list.append([element for element in temp])
			temp.clear()
		else:
			temp.append(each_line)
	if len(temp):
		new_list.append([element for element in temp])
	content = new_list
	for line in content[0]:
		line = line.split(' ')
		range_pair = []
		for seed in line:
			try:
				seeds.append({'seed': int(seed)})
			except ValueError:
				pass
	del content[0]
	for type_of_map in content:
		temp = type_of_map[0].split(' ')
		temp = [temp[0]]
		temp = temp[0].split('-')
		del temp[1]
		source = temp[0]
		destination = temp[1]
		del type_of_map[0]
		for each_map in type_of_map:
			temp = each_map.split(' ')
			temp = [int(element) for element in temp]
			destination_start = temp[0]
			source_start = temp[1]
			range_length = temp[2]
			for index_of_seed in range(len(seeds)):
				if seeds[index_of_seed][source] >= source_start and seeds[index_of_seed][source] < source_start + range_length:
					seeds[index_of_seed][destination] = seeds[index_of_seed][source] + destination_start - source_start
				else:
					if destination not in seeds[index_of_seed]:
						seeds[index_of_seed][destination] = seeds[index_of_seed][source]
		if destination == "location":
			break
seeds.sort(reverse=False, key=lambda element:element["location"])
print(seeds[0]["location"])