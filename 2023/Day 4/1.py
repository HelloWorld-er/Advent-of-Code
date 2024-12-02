total = 0


def count_score():
	global nums_of_win
	if nums_of_win == 0:
		return 0
	score = 1
	nums_of_win -= 1
	while nums_of_win:
		score *= 2
		nums_of_win -= 1
	return score


with open("../input/input4.txt", "r") as file_input:
	cards = []
	for each_card in file_input:
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
		total += count_score()
		
				
print(total)
