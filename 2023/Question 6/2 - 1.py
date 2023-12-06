total = 1

with open("../input/input6.txt", "r") as file_input:
	temp = file_input.readlines()
	temp = [element.strip() for element in temp]
	temp = [element for element in temp if element != ""]
	temp_times = temp[0].split(" ")
	temp_distances = temp[1].split(" ")
	del temp_times[0]
	del temp_distances[0]
	real_time = int(''.join(temp_times))
	real_distance = int(''.join(temp_distances))
	start = -1
	end = -1
	for time_of_hold in range(1, real_time):
		if (real_time - time_of_hold) * time_of_hold > real_distance:
			start = time_of_hold
			break
	for time_of_hold in range(real_time - 1, 0, -1):
		if (real_time - time_of_hold) * time_of_hold > real_distance:
			end = time_of_hold
			break
	total = end - start + 1

print(total)
