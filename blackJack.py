# Пишу мини-вариант игры 'Блэкдек' - 'очко'

import random

import os
clear = lambda: os.system('cls')

def checkCard(c):
	if c == 2:
		print('Вам выпал')
	elif c == 3:
		print('Вам выпала Дама')
	elif c == 4:
		print('Вам выпал Король')
	elif c == 6:
		print('Вам выпала Шестерка')
	elif c == 7:
		print('Вам выпала Семерка')
	elif c == 8:
		print('Вам выпала Восьмерка')
	elif c == 9:
		print('Вам выпала Девятка')
	elif c == 10:
		print('Вам выпала Десятка')
	elif c == 11:
		print('Вам выпал Туз')



def theGame():
	# cards = [2, 3, 4, 6, 7, 8, 9, 10, 11]
	# random.shuffle(cards)
	
	score = 0

	while score <= 21:

		cards = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
		random.shuffle(cards)

		check = str(input('Хотите взять карту? Y или N: '))

		if check == 'Y' or check == 'y':

			card = cards.pop()
			score += card

			if score == 21:

				print('Победа! Ваш счет = 21 !')
				heh()
				
			checkCard(card)
			print('Теперь ваш счет:', score)

		elif check == 'N' or check == 'n':

			print('У вас', score, 'очков')

	else:

		print('К сожалению, перебор. Ваш счет равен', score, 'Вы проиграли')


theGame()

def heh():
	exit = input('Нажмите Enter, чтобы выйти из программы или напишите M, чтобы начать заново: ')

	while exit != 0:

		if exit == 'M' or exit == 'm':
			clear()
			theGame()
		else:
			pass

heh()


# cards = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
# random.shuffle(cards)

# print(cards)


