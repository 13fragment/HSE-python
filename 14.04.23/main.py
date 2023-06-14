import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df_1=pd.read_excel('sales.xlsx')

# task 1 - line graph
# x=['september', 'november', 'march']
# y=[df_1['september'].sum(), df_1['november'].sum(), df_1['march'].sum()]
# plt.xlabel('Месяц')
# plt.ylabel('Объем продаж')
# plt.title('Объем продаж 2021')
# plt.plot(x,y,marker='o')
# plt.show()

# task 2 - bar chart
# x=['september', 'november', 'march']
# y=[df_1['september'].mean(), df_1['november'].mean(), df_1['march'].mean()]
# plt.bar(x,y, label ='Средняя величина прибыли')
# plt.xlabel('Месяц')
# plt.ylabel('Прибыль столбчатой диаграммы')
# plt.title('Пример столбчатой диаграммы')
# plt.legend()
# plt.show()

# task 3 - another bar chart
month=[f'август','сентябрь', 'октябрь', 'декабрь','январь' ]
g1=[200,300,700,400,200]
g2=[340,765,231,432,800]
width=0.2
x=np.arange(len(month))
print(x)
fig,ax=plt.subplots()
rects1=ax.bar(x+width/2,g1,width,label='отдел 1',color='r')
rects2=ax.bar(x-width/2,g2,width,label='отдел 2',color='g')
ax.set_title('Выручка')
ax.set_xticks(x)
ax.set_xticklabels(month)
ax.legend()
plt.show()

# task 4 - pie chart
# x=['september', 'november', 'march']
# y=[df_1['september'].mean(), df_1['november'].mean(), df_1['march'].mean()]
# plt.pie(y,labels=x, autopct='%.1f')
# plt.title('Пример круговой диаграммы')
# plt.show()