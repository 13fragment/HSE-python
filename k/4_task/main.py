n=int(input())
def check(n):
        if n<10:
            return n
        else:
            return n%10+check(n//10)
for i in range(10**(n-1),10**n,1):
    if check(i)==n:
        print(i)