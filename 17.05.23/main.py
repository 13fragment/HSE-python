#task1
dictionary ={}
dictionary ={'cupcake' :'кекс' ,'fatigue' :'усталость', 'cat' :'кот' ,'dog' :'собака' ,'fish' :'рыба', 'sadness' :'грусть'}
print(len(dictionary))
print(' ')
for k ,i in dictionary.items():
    print(k ,' ' ,i)
print(' ')
dictionary['summer' ] ='лето'
dictionary['winter' ] ='зима'
for k ,i in dictionary.items():
    print(k ,' ' ,i)
print(' ')
dictionary.pop('summer' ,'лето')
for k ,i in dictionary.items():
    print(k ,' ' ,i)
print(' ')
inverse_dictionary ={}
for k ,i in dictionary.items():
    inverse_dictionary[i ] =k
for k ,i in inverse_dictionary.items():
    print(k ,' ' ,i)

#task2
def my_power(a, n):
    if (n == 1):
        return (a)
    if (n != 1):
        return (a * my_power(a, n - 1))
a = int(input("Введите число: "))
n = int(input("Введите его степень: "))
print("Результат:", my_power(a, n))

#task3
def stroka(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + stroka(s[1:-1]) + ')' + s[-1]
print(stroka(input()))

#task4
from itertools import permutations
N = int(input())
alphabet = ""
for i in range(1, N + 1):
    alphabet += str(i)
for i in permutations(alphabet, N):
    print(''.join(i))

