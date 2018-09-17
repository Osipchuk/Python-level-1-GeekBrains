# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('Задание 1')


def my_round(number, ndigits=0):
    number *= 10 ** ndigits
    i = number - int(number)
    if i >= 0.5:
        number = int(number) + 1
    else:
        number = int(number)
    return number / 10 ** ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print('\nЗадание 2')


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    if len(ticket_number) != 6:
        return 'Неверный номер билета!'
    left_sum = 0
    right_sum = 0
    for i in range(3):
        left_sum += int(ticket_number[i])
        right_sum += int(ticket_number[i + 3])
    if left_sum == right_sum:
        return 'Поздравляем, вы вытянули счастливый билет!'
    else:
        return 'В следующий раз повезет((('


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
