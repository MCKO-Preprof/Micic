import csv
#открываем нужный файл
with open('space.csv',encoding='utf-8') as f:
    data = list(csv.reader(f,delimiter='*'))
    #создаем ввод
    vod = input()
    spisok_korablei = []
    #заполняем список всех имен кораблей
    for i in data[1:]:
        spisok_korablei.append(i[0])
    #создаем цикл длфя проверки имени и сущестования корабля
    while vod != 'stop':
        for stroka in data[1:]:
            if vod in stroka[0]:
                print(f'Корабль {stroka[0]} был отправлен с планеты: {stroka[1]} и его направление движения было: {stroka[-1]}')
                continue
            if vod not in spisok_korablei:
                print('error')
                vod = input()
        vod = input()
