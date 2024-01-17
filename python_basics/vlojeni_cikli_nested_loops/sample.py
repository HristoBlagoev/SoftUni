destination = input()  # това ти е еквивалент на command, който се презаписва накрая на цикъла

while destination != 'End':  # трябва ти цикъл, който проверява дали command/destination e 'End'
    min_budget = float(input())  # трябва да е float иначе ще получиш Runtime error на скрити тестове
    needed_money = 0

    while min_budget > needed_money:  # не трябва да влиза в цикъла когато са равни
        tips = float(input())  # същата работа като min_budget - ще се чудиш защо гърми
        needed_money += tips

    print(f'Going to {destination}!')  # достига се и печата, когато вложеният цикъл приключи

    destination = input() # презаписва се и ако е 'End' програмата приключва, иначе започва от начало