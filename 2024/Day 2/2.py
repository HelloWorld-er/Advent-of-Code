with open("../input/input2.txt") as f:
    safe_reports_number = 0
    for report in f:
        levels_list = list(map(int, report.strip().split(" ")))
        if len(levels_list) < 2:
            safe_reports_number += 1
            continue
        for i in range(len(levels_list), -1, -1):
            new_list = [levels_list[j] for j in range(len(levels_list)) if j != i]
            if new_list[0] > new_list[1]:
                ascending_trend = False
            else:
                ascending_trend = True
            is_safe = True
            for level_index in range(len(new_list) - 1):
                if ascending_trend and new_list[level_index] > new_list[level_index + 1]:
                    is_safe = False
                    break
                if ascending_trend is False and new_list[level_index] < new_list[level_index + 1]:
                    is_safe = False
                    break
                if not (1 <= abs(new_list[level_index] - new_list[level_index + 1]) <= 3):
                    is_safe = False
                    break
            if is_safe:
                safe_reports_number += 1
                break
    print(safe_reports_number)
