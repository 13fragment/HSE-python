from random import randint
n = int(input())
a = [0]*n
for i in range(n):
    a[i] = randint(0,99)
c = a.index(max(a))
for m in range(len(a)-c):
    if max(a)>a[c+m]:
        a[c+m]=0
print(a)

            

        
    
