

with open("../input/input2.txt") as f:
    safe_reports_number = 0
    for report in f:
        levels_list = list(map(int, report.strip().split(" ")))
        if len(levels_list) < 2:
            safe_reports_number += 1
            continue
        if levels_list[0] > levels_list[1]:
            ascending_trend = False
        else:
            ascending_trend = True
        is_safe = True
        for level_index in range(len(levels_list) - 1):
            if ascending_trend and levels_list[level_index] > levels_list[level_index + 1]:
                is_safe = False
                break
            if ascending_trend is False and levels_list[level_index] < levels_list[level_index + 1]:
                is_safe = False
                break
            if not (1 <= abs(levels_list[level_index] - levels_list[level_index + 1]) <= 3):
                is_safe = False
                break
        if is_safe:
            safe_reports_number += 1
    print(safe_reports_number)

