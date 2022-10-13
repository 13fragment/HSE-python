n,m = int(input()), int(input())
a,b = [0]*n,[0]*m
for i in range(n):
    a[i]= int(input())
for l in range(m):
    b[l]=int(input())
for k in range(n):
    for f in range(m):
        if a[k]==b[f]:
            print(a[k])

    



