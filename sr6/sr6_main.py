def vvod():
    global n,m,a,b,g
    n,m,g = int(input('Размерность 1 массива = ',)), int(input('Размерность 2 массива = ',)),0
    a,b = [0]*n,[0]*m
    return a,b,g
vvod()
if (n > 0 or m>0):
    print('Ошибка')
def prints():
    print('Нет совподающих элементов')
for i in range(n):
    a[i] = input('Элемент 1 массива = ')
for l in range(m):
    b[l]=input('Элемент 2 массива = ')
for k in range(n):
    for f in range(m):
        if a[k]==b[f]:
            g = a[k]
            print('Общие элемент массива','',end='',)
            print(a[k])
if g ==0:
    prints() 

    


    