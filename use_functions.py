"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

count = 0
count_rep = 0
count_history = []

def count_management(count):
    cost = int(input('Введите сумму покупки: '))
    if cost > count:
        print('Недостаточно средств. Пополните счёт.')
    else:
        count -= cost
        purchase = input('Что Вы купили?')
        print('Успешная покупка! На счёте осталось: ', cost, 'руб.' )
        count_history.append((purchase, cost))
    return cost

while True:
    print('Доступные операции:')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        count_rep = int(input('Введите сумму пополнения счёта: '))
        count += count_rep
        print(count)
    elif choice == '2':
        count_management(count)
    elif choice == '3':
        print(count_history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')