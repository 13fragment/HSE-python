spisok = list(map(int,input().split(" ")))
spisok.sort()
spisok.reverse()
MashaGrowth = int(input())
print(len(spisok))
for i in range(1,len(spisok)-1):
    if spisok[i-1] < MashaGrowth:
        print(spisok[i])