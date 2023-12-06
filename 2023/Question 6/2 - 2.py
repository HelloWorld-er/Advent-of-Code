def find_start(left, right, real_t, real_d):
	mid = -1
	while left < right:
		mid = (left + right) / 2
		if (real_t - mid) * mid > real_d:
			right = mid
		else:
			left = mid + 1
	return int(mid) + 1


def find_end(left, right, real_t, real_d):
	mid = -1
	while left < right:
		mid = (left + right) / 2
		if (real_t - mid) * mid > real_d:
			left = mid
		else:
			right = mid - 1
	return int(mid)


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
	start = find_start(1, real_time - 1, real_time, real_distance)
	end = find_end(1, real_time - 1, real_time, real_distance)
	total = end - start + 1

print(total)
