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
	i = 0
	for line in content[0]:
		line = line.split(' ')
		range_pair = []
		for seed_info in line:
			try:
				range_pair.append(int(seed_info))
			except ValueError:
				pass
			if len(range_pair) == 2:
				seeds.append({'seed-start': range_pair[0], 'seed-end': range_pair[0] + range_pair[1] - 1})
				range_pair = []
	del content[0]
	relationship_of_sd = []
	for type_of_map in content:
		temp = type_of_map[0].split(' ')
		temp = [temp[0]]
		temp = temp[0].split('-')
		del temp[1]
		source = temp[0]
		destination = temp[1]
		del type_of_map[0]
		# print(seeds)
		relationship_of_sd.append({"convert":(source, destination), "map": []})
		for each_map in type_of_map:
			temp = each_map.split(' ')
			temp = [int(element) for element in temp]
			destination_start = temp[0]
			source_start = temp[1]
			range_length = temp[2]
			relationship_of_sd[-1]["map"].append(destination_start - source_start)
			for index_of_seed in range(len(seeds)):
				if 
				
		if destination == "location-start":
			break
seeds.sort(reverse=False, key=lambda element:element["location-start"])
print(seeds)
print(seeds[0]["location-start"])
