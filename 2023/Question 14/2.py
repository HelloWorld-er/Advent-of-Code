total = 0
rocks_list = []
rocks_dict = {}

with open("../input/input14.txt", "r") as input_file:
	info = input_file.readlines()
	info = [list(line.strip()) for line in info]
	for line_index in range(len(info)):
		for element_index in range(len(info[line_index])):
			if info[line_index][element_index] == 'O':
				rocks_list.append([line_index, element_index])
				rocks_dict[len(rocks_list) - 1] = {"north": [], "south": [], "east": [], "west": []}
	for element_index in range(len(rocks_list)):
		temp_bool = -1
		print(element_index)
		# print()
		while True:
			# print(rocks_list[element_index])
			# north
			x = rocks_list[element_index][1]
			y = rocks_list[element_index][0]
			while y >= 0:
				y -= 1
				if y < 0 or info[y][x] == '#':
					if [y, x] == rocks_dict[element_index]["north"]:
						temp_bool += 1
					rocks_dict[element_index]["north"] = [y, x]
					rocks_list[element_index][0] = y + 1
					rocks_list[element_index][1] = x
					break
			# west
			x = rocks_list[element_index][1]
			y = rocks_list[element_index][0]
			while x >= 0:
				x -= 1
				if x < 0 or info[y][x] == '#':
					if [y, x] == rocks_dict[element_index]["west"]:
						temp_bool += 1
					rocks_dict[element_index]["west"] = [y, x]
					rocks_list[element_index][0] = y
					rocks_list[element_index][1] = x + 1
					break
			# south
			x = rocks_list[element_index][1]
			y = rocks_list[element_index][0]
			while y < len(info):
				y += 1
				if y >= len(info) or info[y][x] == '#':
					if [y, x] == rocks_dict[element_index]["south"]:
						temp_bool += 1
					rocks_dict[element_index]["south"] = [y, x]
					rocks_list[element_index][0] = y - 1
					rocks_list[element_index][1] = x
					break
			# east
			x = rocks_list[element_index][1]
			y = rocks_list[element_index][0]
			while x < len(info[0]):
				x += 1
				if x >= len(info[0]) or info[y][x] == '#':
					if [y, x] == rocks_dict[element_index]["east"]:
						temp_bool += 1
					rocks_dict[element_index]["east"] = [y, x]
					rocks_list[element_index][0] = y
					rocks_list[element_index][1] = x - 1
					break
			# print(rocks_dict[element_index])
			if temp_bool >= 3:
				break
		# print(rocks_dict[element_index])
		total += len(info) - rocks_dict[element_index]["east"][0]
	
	# length = len(info)
	# for line in range(len(info)):
	# 	num = 0
	# 	for element in info[line]:
	# 		if element == 'O':
	# 			num += 1
	# 	total += num * length
	# 	length -= 1
	
	# for line in info:
	# 	print(line)

print(total)
