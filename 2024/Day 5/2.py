def compare(value_a: int, value_b: int) -> bool:
    """If value_a is before value_b, return True, otherwise return False"""
    global page_ordering_rules_dict_bt
    if value_a == value_b:
        return True
    if value_b not in page_ordering_rules_dict_bt:
        return False
    if value_a in page_ordering_rules_dict_bt[value_b]:
        return True
    return False

def sort(sort_list: list, left: int, right: int):
    if right <= left:
        return
    l_pointer = left
    r_pointer = right
    while l_pointer < r_pointer:
        while l_pointer < r_pointer and compare(sort_list[left], sort_list[r_pointer]):
            r_pointer -= 1
        while l_pointer < r_pointer and compare(sort_list[l_pointer], sort_list[left]):
            l_pointer += 1
        sort_list[l_pointer], sort_list[r_pointer] = sort_list[r_pointer], sort_list[l_pointer]
    sort_list[l_pointer], sort_list[left] = sort_list[left], sort_list[l_pointer]
    sort(sort_list, left, l_pointer - 1)
    sort(sort_list, l_pointer + 1, right)
    return

with open("../input/input5.txt") as f:
    sum_of_middle_pages = 0
    f_read_list = f.readlines()
    split_index = f_read_list.index("\n")
    page_ordering_rules_list = [i.strip().split('|') for i in f_read_list[:split_index]]
    page_ordering_rules_list = [(int(item) for item in sublist) for sublist in page_ordering_rules_list]
    update_lists = [[int(j) for j in i.strip().split(',')] for i in f_read_list[split_index + 1:]]
    page_ordering_rules_dict_tb = {} # tb means top to bottom
    for key, value in page_ordering_rules_list:
        if key in page_ordering_rules_dict_tb:
            page_ordering_rules_dict_tb[key].add(value)
        else:
            page_ordering_rules_dict_tb[key] = {value}
    page_ordering_rules_dict_bt = {} # bt means bottom to top
    for key, value in page_ordering_rules_dict_tb.items():
        for item in page_ordering_rules_dict_tb[key]:
            if item in page_ordering_rules_dict_bt:
                page_ordering_rules_dict_bt[item].add(key)
            else:
                page_ordering_rules_dict_bt[item] = {key}
    for update_list in update_lists:
        sorted_list = [i for i in update_list]
        sort(sorted_list, 0, len(sorted_list) - 1)
        if sorted_list != update_list:
            sum_of_middle_pages += sorted_list[len(sorted_list) // 2]
    print(sum_of_middle_pages)