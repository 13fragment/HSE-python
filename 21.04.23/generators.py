# n = int(input())
# def xmasTree():
#     return (f"   * \n  *** \n *****\n******* \n")*n
# print(xmasTree())

# n,m = map(int,input().split())
# a = [[(int)(j-i+1)%2 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=" ")
#     print()

# n,m = map(int,input().split())
# f = int()
# a = [[i*4+j+1 for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=" ")
#     print()

n,m = map(int,input().split())
f = int()
a = [[(i)+(j*5) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(a[i][j],end=" ")
    print()