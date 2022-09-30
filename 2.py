katet1,katet2,gypotenuza = float(input('Катет 1 = ')),float(input('Катет 2 = ')) ,float(input('Гипотенуза = ')) 
square = 0
if katet1**2 + katet2**2 == gypotenuza**2:
    square = katet1*katet2/2
    print(square)
else:
    print('Ошибка, данный треугольник не является прямоугольным')

