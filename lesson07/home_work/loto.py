#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:
    def __init__(self, player_name):
        self.player_name = player_name
        self.nums = 15
        self.check = 0
        self.rows = []
        self.numbers = []

    def create_card(self):
        while len(self.numbers) < self.nums:
            number = random.randint(1, 90)
            if number not in self.numbers:
                self.numbers.append(number)
        self.rows = [sorted(self.numbers[:5]), sorted(self.numbers[5:10]), sorted(self.numbers[10:])]

    def del_num(self, num):
        del_count = 0
        for row in self.rows:
            if num in row:
                row[row.index(num)] = 'X'
                del_count = 1
                self.check += 1
                break
        if del_count != 1:
            print(f'{self.player_name} проиграл')

    def check_barrel(self, num):
        for row in self.rows:
            if num in row:
                return True
        return False

    def print_card(self):
        card_name = f'====== {self.player_name} ======'
        print(card_name)
        for row in self.rows:
            for num in row:
                print(f' {num} ', end='')
            print()
        print(f'Незачеркнуто номеров {15 - self.check}')
        print('=' * len(card_name))


class Bot:
    def __init__(self, name, card):
        self.card = card
        self.name = name

    def action(self, num):
        if self.card.check_barrel(num):
            self.card.del_num(num)
        else:
            print('Не зачеркиваю')

answer = input('Хотите сыграть в лото? Y/N: \n').upper()
if answer == 'Y':
    Player = Card(input('Введите ваше имя: \n'))
    bot_name = input('Введите имя противника: \n')
    bot = Bot(bot_name, Card(bot_name))


while answer == 'Y':
    bot.card.create_card()
    Player.create_card()
    barrels = [x for x in range(1, 91)]
    while Player.check < 15 and bot.card.check < 15:
        print(f'В мешке осталось {len(barrels)} бочонков')
        Player.print_card()
        bot.card.print_card()
        barrel = random.choice(barrels)
        print(f'Выпал бочонок № {barrel}')
        barrels.remove(barrel)
        choise = input('Хотите вычеркнуть номер? Y/N: \n').upper()
        if choise == 'Y':
            if not Player.check_barrel(barrel):
                print('Такого номера нет. Вы проиграли')
                print(f'В мешке остали бочонки: {barrels}')
                break
            Player.del_num(barrel)
        else:
            if Player.check_barrel(barrel):
                print('У вас есть такой номер. Вы проиграли')
                print(f'В мешке остали бочонки: {barrels}')
                break
        print(f'Очередь игрока {bot.name}')
        bot.action(barrel)
        if Player.check >= 15 and bot.card.check >= 15:
            print('Победила дружба')
            print(f'В мешке остали бочонки: {barrels}')
        elif Player.check >= 15:
            print(f'Победил {Player.player_name}')
            print(f'В мешке остали бочонки: {barrels}')
        elif bot.card.check >= 15:
            print(f'Победил {bot.name}')
            print(f'В мешке остали бочонки: {barrels}')
    answer = input('Хотите сыграть в еще раз? Y/N: \n').upper()
print('Спасибо за игру!')
