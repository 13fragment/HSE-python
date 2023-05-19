import pandas as pd
df1 = pd.concat(pd.read_excel('Table1.xlsx', sheet_name=None), ignore_index=True)
indexes = list()
print(df1.loc[(df1['Группа']=='22БИ-1')&(df1['Оценка за экзамен']>=8)])