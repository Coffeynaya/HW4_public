"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')
'''

'''

def burn_date(q_1 = 'Введите год рождения А.С. Пушкина: ', q_2 = 'В какой день родился А.С. Пушкин? '):
    date_1 = 1799
    date_2 = 6

    answer_1 = int(input(q_1))
    while answer_1 != date_1:
        print('Не верно')
        answer_1 = int(input(q_1))
    answer_2 = int(input(q_2))
    while answer_2 != date_2:
        print('Не верно')
        answer_2 = int(input(q_2))
    print('Верно!')

    print('Спасибо за игру!')


burn_date()

