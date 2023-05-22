#task1
def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 7:
            print("Password should have at least 7 letters")
        elif not any(chr.isdigit() for chr in password):
            print("Password should have at least 1 number")
        elif not any(chr.isupper() for chr in password):
            print("Password should have at least 1 uppercase letter")
        elif not any(chr.islower() for chr in password):
            print("Password should have at least 1 lowercase letter")
        else:
            print("Your password seems fine")
            break

validate()

#task2
s = input()
a=[]
for i in range(len(s)):
  for j in range(len(s)):
   if s[i] == s[j]:
    if len(s[i:j+1])>len(a):
      a.append(s[i:j+1])
print(max(a,key=len))

#task3
students_height = [int(i) for i in input().split()]
height = int(input())
pos = 0
for i in range(len(students_height) + 1):
    if students_height[i] > 200 or students_height[i] < 0:
        print("Рост не должен превышать 200 см или быть отрицательным")
        break
    if students_height[i]== height:
        pos += 1
    print(pos + 1)
    break
