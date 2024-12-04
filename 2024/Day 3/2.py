import re

with open("../input/input3.txt") as f:
    total = 0
    multiply_matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", f.read())
    do = True
    for match in multiply_matches:
        if match == "don't()":
            do = False
        elif match == "do()":
            do = True
        elif do:
            a, b = re.findall(r"(\d+)", match)
            total += int(a) * int(b)
    print(total)