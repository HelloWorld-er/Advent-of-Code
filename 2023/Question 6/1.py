total = 1

with open("../input/input6.txt", "r") as file_input:
	temp = file_input.readlines()
	temp = [element.strip() for element in temp]
	temp = [element for element in temp if element != ""]
	times = temp[0].split(" ")
	distances = temp[1].split(" ")
	del times[0]
	del distances[0]
	times = [int(element) for element in times if element != ""]
	distances = [int(element) for element in distances if element != ""]
	solution = 0
	for race in range(len(times)):
		time = times[race]
		distance = distances[race]
		start = -1
		end = -1
		for time_of_hold in range(1, time):
			if (time - time_of_hold) * time_of_hold > distance:
				start = time_of_hold
				break
		for time_of_hold in range(time - 1, 0, -1):
			if (time - time_of_hold) * time_of_hold > distance:
				end = time_of_hold
				break
		solution = end - start + 1
		total *= solution

print(total)
