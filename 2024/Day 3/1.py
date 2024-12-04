import re

with open("../input/input3.txt") as f:
    total = 0
    multiply_matches = re.findall(r"mul\(\d+,\d+\)", f.read())
    for match in multiply_matches:
        a, b = re.findall(r"(\d+)", match)
        total += int(a) * int(b)
    print(total)