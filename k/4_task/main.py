n = int(input())
numb = 0
for i in range(10 ** (n - 1), 10 ** n, 1):
    numb = i
    summa = 0
    while numb > 0:
        summa += numb % 10
        numb //= 10
    if summa == n:
        print(i)
