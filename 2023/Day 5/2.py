seeds = []

def reload(temp_dict, difference_start, difference_end, position):
	copy_dict = {element[0]: element[1] for element in temp_dict.items()}
	for item in copy_dict.items():
		if item[0] == position[0] + "-start" or item[0] == position[0] + "-end":
			continue
		if item[0] == position[1] + "-start" or item[0] == position[0] + "-end":
			continue
		if "-start" in item[0]:
			temp_dict[item[0]] += difference_start
		elif "-end" in item[0]:
			temp_dict[item[0]] += difference_end
	return temp_dict


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
				if seeds[index_of_seed][source + "-start"] < source_start:
					if seeds[index_of_seed][source + "-end"] < source_start:
						if destination + "-start" not in seeds[index_of_seed]:
							seeds[index_of_seed][destination + "-start"] = seeds[index_of_seed][source + "-start"]
							seeds[index_of_seed][destination + "-end"] = seeds[index_of_seed][source + "-end"]
					else:
						temp_start = seeds[index_of_seed][source + "-start"]
						temp_end = seeds[index_of_seed][source + "-end"]
						seeds.append({element[0]: element[1] for element in seeds[index_of_seed].items()})
						seeds[-1][source + "-start"] = source_start
						seeds[index_of_seed][source + "-end"] = source_start - 1
						if seeds[-1][source + "-end"] >= source_start + range_length:
							seeds.append({element[0]: element[1] for element in seeds[-1].items()})
							seeds[-1][source + "-start"] = source_start + range_length
							seeds[-2][source + "-end"] = source_start + range_length - 1
							seeds[-2][destination + "-start"] = seeds[-2][source + "-start"] + relationship_of_sd[-1]["map"][-1]
							seeds[-2][destination + "-end"] = seeds[-2][source + "-end"] + relationship_of_sd[-1]["map"][-1]
							seeds[-1][destination + "-start"] = seeds[-1][source + "-start"]
							seeds[-1][destination + "-end"] = seeds[-1][source + "-end"]
							seeds[-1] = reload(seeds[-1], seeds[-1][source + "-start"] - temp_start, seeds[-1][source + "-end"] - temp_end, (source, destination))
							seeds[-2] = reload(seeds[-2], seeds[-2][source + "-start"] - temp_start, seeds[-2][source + "-end"] - temp_end, (source, destination))
						else:
							seeds[-1][destination + "-start"] = seeds[-1][source + "-start"] + relationship_of_sd[-1]["map"][-1]
							seeds[-1][destination + "-end"] = seeds[-1][source + "-end"] + relationship_of_sd[-1]["map"][-1]
							seeds[-1] = reload(seeds[-1], seeds[-1][source + "-start"] - temp_start, seeds[-1][source + "-end"] - temp_end, (source, destination))
						seeds[index_of_seed][destination + "-start"] = seeds[index_of_seed][source + "-start"]
						seeds[index_of_seed][destination + "-end"] = seeds[index_of_seed][source + "-end"]
						seeds[index_of_seed] = reload(seeds[index_of_seed], seeds[index_of_seed][source + "-start"] - temp_start, seeds[index_of_seed][source + "-end"] - temp_end, (source, destination))
				elif seeds[index_of_seed][source + "-start"] < source_start + range_length:
					if seeds[index_of_seed][source + "-end"] < source_start + range_length:
						seeds[index_of_seed][destination + "-start"] = seeds[index_of_seed][source + "-start"] + relationship_of_sd[-1]["map"][-1]
						seeds[index_of_seed][destination + "-end"] = seeds[index_of_seed][source + "-end"] + relationship_of_sd[-1]["map"][-1]
					else:
						temp_start = seeds[index_of_seed][source + "-start"]
						temp_end = seeds[index_of_seed][source + "-end"]
						seeds.append({element[0]: element[1] for element in seeds[index_of_seed].items()})
						seeds[-1][source + "-start"] = source_start + range_length
						seeds[index_of_seed][source + "-end"] = source_start + range_length - 1
						seeds[index_of_seed][destination + "-start"] = seeds[index_of_seed][source + "-start"] + relationship_of_sd[-1]["map"][-1]
						seeds[index_of_seed][destination + "-end"] = seeds[index_of_seed][source + "-end"] + relationship_of_sd[-1]["map"][-1]
						seeds[-1][destination + "-start"] = seeds[-1][source + "-start"]
						seeds[-1][destination + "-end"] = seeds[-1][source + "-end"]
						seeds[-1] = reload(seeds[-1], seeds[-1][source + "-start"] - temp_start, seeds[-1][source + "-end"] - temp_end, (source, destination))
						seeds[index_of_seed] = reload(seeds[index_of_seed], seeds[index_of_seed][source + "-start"] - temp_start, seeds[index_of_seed][source + "-end"] - temp_end, (source, destination))
				else:
					if destination + "-start" not in seeds[index_of_seed]:
						seeds[index_of_seed][destination + "-start"] = seeds[index_of_seed][source + "-start"]
						seeds[index_of_seed][destination + "-end"] = seeds[index_of_seed][source + "-end"]
		if destination == "location-start":
			break
seeds.sort(reverse=False, key=lambda element:element["location-start"])
print(seeds[0]["location-start"])
