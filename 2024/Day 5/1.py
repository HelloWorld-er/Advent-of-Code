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
        is_right_order = True
        for update_item_index in range(len(update_list) - 1):
            if update_list[update_item_index + 1] not in page_ordering_rules_dict_bt:
                is_right_order = False
                break
            if  not (update_list[update_item_index] in page_ordering_rules_dict_bt[update_list[update_item_index + 1]]):
                is_right_order = False
                break
        if is_right_order:
            sum_of_middle_pages += update_list[len(update_list) // 2]
    print(sum_of_middle_pages)