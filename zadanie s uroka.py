a,b,t = 2,5,8
print(a,b,t)
while a != 5 and b != 2:
    a,b = str(a), str(b)
    #  a = 5, b = 2
    a = a.replace('2','5',1)
    b = b.replace('5','2',1)
    a,b = int(a), int(b)
print(a,b,t)