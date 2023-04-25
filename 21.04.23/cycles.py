# print("Введите число")
# number = int(input())
# k = number
# result = list()
# while k != 0:
#     if number %k ==0:
#         result.append(k)
#     k = k-1
# print(result)


# print("KPH","MPH")
# kph = int()
# for kph in range(1,300):
#     print(kph,round(kph*0.6214,1))


# n = int(input())
# a = list()
# for i in range(1,n):
#     k = i**2
#     if k <n:
#         a.append(k)
# print(a)

# n = int(input())
# a = list(map(int,input().split(" ")))
# k = int()
# for i in range(0,n):
#     if a[i-1] <= a[i] and k<a[i]:
#         k = a[i]
# print(a.index(k)) # в задании ошибка, исходя из теории масивов (а конкретнее списков в Python) нумерация элементов идет с 0 => наибольший элемент из набора 5 4 3 2 1 3 будет с индексом 0


# a = list(map(int,input().split(" ")))
# a.append(0)
# k = int()
# for i in range(1,len(a)-1):
#     if a[i] %2 ==0:
#         k+=1
# print(k)