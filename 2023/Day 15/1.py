total = 0

with open("../input/input15.txt", "r") as input_file:
    info = input_file.readline().split(',')
    for case_index in range(len(info)):
       num = 0
       for element_index in range(len(info[case_index])):
          num += ord(info[case_index][element_index])
          num *= 17
          num %= 256
       total += num

print(total)
