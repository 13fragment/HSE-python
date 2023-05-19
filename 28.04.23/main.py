sales_file = open("customer.txt","r""+")
num_days = int(input("Введите количество дней с продажами: "))
salesVolume = list()
for court in range(1,num_days+1):
    sales = int(input(f"Введите количество продаж за {court} день: "))
    salesVolume.append(sales)
    sales_file.write(f"Объем продаж за {court} день: "+str(sales)+"\n")
sales_file.close()
print("Минимальный объем продаж за все дни: "+min(salesVolume))
print("Максимальный объем продаж за все дни: "+max(salesVolume))
sum = int()
for i in range(len(salesVolume)):
    sum+=salesVolume[i]
print("Суммарный объем продаж: "+sum)
#Пускай продаем товары по 5$
print("Было продана товаров на сумму: "+sum*5+"$")

    