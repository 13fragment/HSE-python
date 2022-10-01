# взял в среднем что в году 365 дней
uslovie = 8*60/5 #исходя из условия столько человек в среднем может посмотреть экспонатов за 1 день
kolvoExp,kolvoVremeni = int(input('Количество экспонатов = ')), int(input('Количество лет = ' ))
k = 0
# if kolvoVremeni | kolvoExp <=0:
#     print('Ошибка, введены неверные значения') можно сделать такой вариант более короткий но не более явный для пользователя
# а можно сделать так
if kolvoExp < 0:
    print('Ошибка, введено неверное значение экспонатов')
elif kolvoVremeni < 0:
    print('Ошибка, введено неверное значение времени')
elif kolvoVremeni==kolvoExp==0:
    print('Ошибка, введены неверные значение экспонатов и времени')
if kolvoExp > 0 & kolvoVremeni >=0:
    k = kolvoExp / uslovie
    print('Понадобится времени что осмотреть все экспонаты в днях = ',k)
if kolvoVremeni > 0 & kolvoExp>=0:
    kolvoVremeni = kolvoVremeni*365*24
    k = kolvoVremeni * uslovie
    print('Кол-во экспонатов, осмотренных по заданому времени равно = ',k)

