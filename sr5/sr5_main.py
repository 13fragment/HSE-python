a,b = int(input()),int(input())
c = ''
while a >0:
    k = a%b
    a = a//b
    c+=str(k)
def reverseFunction(c):
    return c[::-1]
print(reverseFunction(c))
