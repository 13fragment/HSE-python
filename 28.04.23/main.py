# task 1
# sales_file = open("customer.txt","r""+")
# num_days = int(input("Введите количество дней с продажами: "))
# salesVolume = list()
# for court in range(1,num_days+1):
#     sales = int(input(f"Введите количество продаж за {court} день: "))
#     salesVolume.append(sales)
#     sales_file.write(f"Объем продаж за {court} день: "+str(sales)+"\n")
# sales_file.close()
# print("Минимальный объем продаж за все дни: "+min(salesVolume))
# print("Максимальный объем продаж за все дни: "+max(salesVolume))
# sum = int()
# for i in range(len(salesVolume)):
#     sum+=salesVolume[i]
# print("Суммарный объем продаж: "+sum)
# #Пускай продаем товары по 5$
# print("Было продана товаров на сумму: "+sum*5+"$")

# task 2
# users=open('users.txt','w')
# surname=["Щапова", "Жулитова", "Маслинова", "Чумазина"]
# name=["Майя", "Дарья", "Софья", "Снежанна"]
# middleName=["Алексеевна", "Алексеевна", "Петровна", "Владимировна"]
# year=[2004,2004,2004,2003]
# city=["Нижний Новгород", "Нижний Новгород", "Дзержинск", "Нижний Новгород"]
# for index in range(len(surname)):
#     users.write(str(surname[index]) + " " + str(name[index]) + " " + str(middleName[index]) + " " + str(year[index]) + " " + str(city[index]) + " "+ '\n' )
# users.close()
# users=open('users.txt','r')
# lines=users.readlines()
# A=[]
# for line in lines:
#   line=line.split(' ')
#   A+=([line[3]])
# print(A)

# task 3
infile=open('words.txt','r')
l1=infile.readline().rstrip('\n').split()
l2=infile.readline().rstrip('\n').split()
l3=infile.readline().rstrip('\n').split()
A=l1+l2+l3
infile.close()
max=0
for i in range (len(A)):
  if len(A[i])>max:
    max=len(A[i])
print(max, A[i])



    