total = 0

with open("../input/input4.txt", "r") as file_input:
	cards = []
	num_of_card = 0
	for each_card in file_input:
		num_of_card += 1
		each_card = each_card.split(':')
		del each_card[0]
		each_card = each_card[0].split('|')
		winning_numbers = each_card[0].split(' ')
		user_numbers = each_card[1].strip().split(' ')
		index = 0
		while index < len(winning_numbers):
			if winning_numbers[index] == '':
				del winning_numbers[index]
				index -= 1
			index += 1
		index = 0
		winning_numbers = [int(str_num) for str_num in winning_numbers]
		while index < len(user_numbers):
			if user_numbers[index] == '':
				del user_numbers[index]
				index -= 1
			index += 1
		user_numbers = [int(str_num) for str_num in user_numbers]
		nums_of_win = 0
		for win_num in winning_numbers:
			for user_num in user_numbers:
				if win_num == user_num:
					nums_of_win += 1
		while True:
			if num_of_card + nums_of_win <= len(cards):
				break
			cards.append(1)
		for index in range(num_of_card, num_of_card + nums_of_win):
			cards[index] += cards[num_of_card - 1]
		total += cards[num_of_card - 1]
			

print(total)
