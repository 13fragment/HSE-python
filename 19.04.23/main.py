# k1,k2,k3,k4,k5 = int(input()),int(input()),int(input()),int(input()),int(input())
# print((k1+k2+k3+k4+k5)/5)
# print("Congrats") if (k1+k2+k3+k4+k5)/5>=8 else None



# salary,years = int(input()),int(input())
# print("Ваша ссуда одобрена") if (years >=2 and salary>30000) or (years<1 and salary>30000) else print("Вы должны поработать не менее 2 лет") if salary>=30000 else print("Вы должны зарабатывать > 30000$")


# points = int(input())
# if points > 90: print("A")
# elif 80<=points<=89: print("B")
# elif 70<=points<=79: print("C")
# elif 60<=points<=69: print("D")
# else: print("F")

x = list(map(int,input().split(" ")))
if (len(x)>4):
    SystemExit
else:
    indexMax = x.index(max(x))
    x[0],x[indexMax] = x[indexMax],x[0]
    indexMin = x.index(min(x))
    x[3], x[indexMin] = x[indexMin], x[3]
    if x[1] <= x[2]:
        x[1],x[2] = x[2],x[1]
print(x)