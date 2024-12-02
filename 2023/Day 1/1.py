total = 0
with open("../input/input1.txt", "r") as file_input:
    for content in file_input:
        calibration_value = 0
        for char in content:
            try:
                calibration_value = int(char)
                break
            except ValueError:
                pass
        calibration_value *= 10
        for step in range(len(content) - 1, -1, -1):
            try:
                calibration_value += int(content[step])
                break
            except ValueError:
                pass
        total += calibration_value
print(total)