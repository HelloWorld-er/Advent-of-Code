total = 0

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def compare(x, y):
	global hands, cards
	list_x = [element for element in x[0]]
	list_y = [element for element in y[0]]
	bucket_x = {card: 0 for card in cards}
	bucket_y = {card: 0 for card in cards}
	for card_index in range(len(list_x)):
		bucket_x[list_x[card_index]] += 1
		bucket_y[list_y[card_index]] += 1
	
	j_card_num_x = bucket_x['J']
	j_card_num_y = bucket_y['J']
	
	list_bucket_x = sorted(list(bucket_x.items()), reverse=True, key=lambda element: element[1])
	list_bucket_y = sorted(list(bucket_y.items()), reverse=True, key=lambda element: element[1])
	
	list_bucket_x = [[element[0], element[1]] for element in list_bucket_x]
	list_bucket_y = [[element[0], element[1]] for element in list_bucket_y]
	
	if list_bucket_x[0][0] == 'J':
		list_bucket_x[1][1] += j_card_num_x
		list_bucket_x.append(['J', 0])
		del list_bucket_x[0]
	else:
		list_bucket_x[0][1] += j_card_num_x
		del list_bucket_x[list_bucket_x.index(['J', j_card_num_x])]
	
	if list_bucket_y[0][0] == 'J':
		list_bucket_y[1][1] += j_card_num_y
		list_bucket_y.append(['J', 0])
		del list_bucket_y[0]
	else:
		list_bucket_y[0][1] += j_card_num_y
		del list_bucket_y[list_bucket_y.index(['J', j_card_num_y])]
	
	if list_bucket_x[0][1] == 5:
		type_x = 6
	elif list_bucket_x[0][1] == 4:
		type_x = 5
	elif list_bucket_x[0][1] == 3 and list_bucket_x[1][1] == 2:
		type_x = 4
	elif list_bucket_x[0][1] == 3:
		type_x = 3
	elif list_bucket_x[0][1] == 2 and list_bucket_x[1][1] == 2:
		type_x = 2
	elif list_bucket_x[0][1] == 2:
		type_x = 1
	else:
		type_x = 0
	
	if list_bucket_y[0][1] == 5:
		type_y = 6
	elif list_bucket_y[0][1] == 4:
		type_y = 5
	elif list_bucket_y[0][1] == 3 and list_bucket_y[1][1] == 2:
		type_y = 4
	elif list_bucket_y[0][1] == 3:
		type_y = 3
	elif list_bucket_y[0][1] == 2 and list_bucket_y[1][1] == 2:
		type_y = 2
	elif list_bucket_y[0][1] == 2:
		type_y = 1
	else:
		type_y = 0
	
	if type_x > type_y:
		return True
	elif type_x < type_y:
		return False
	else:
		for card_index in range(len(list_x)):
			index_x = cards.index(list_x[card_index])
			index_y = cards.index(list_y[card_index])
			if index_x < index_y:
				return True
			elif index_x > index_y:
				return False
		return "same"


def sort_hands(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if compare(x, pivot) is False]
	middle = [x for x in arr if compare(x, pivot) == "same"]
	right = [x for x in arr if compare(x, pivot) is True]
	return sort_hands(left) + middle + sort_hands(right)


with open("../input/input7.txt", "r") as file_input:
	hands = []
	for hand in file_input:
		hands.append(list(hand.split(' ')))
	hands = sort_hands(hands)
	for rank in range(1, len(hands) + 1):
		result = int(hands[rank - 1][1].strip())
		total += result * rank

print(total)
