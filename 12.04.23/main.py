# For working correctly this modules should be pre-installed to the interpreter: pandas/openpyxl
# Use pip install for installing pandas and openpyxl
import pandas as pd

df1 = pd.read_excel("sales.xlsx",sheet_name="shop1")
df2 = pd.read_excel("sales.xlsx",sheet_name="shop2")
df3 = pd.read_excel("sales.xlsx",sheet_name="shop3")

# Connect 3 df together
df_merged = pd.concat([df1,df2,df3],axis=0,ignore_index=True)

# Add new column
df_merged["New row"] = [10,20,12,30,120123,123,123,12312,31,23,123,12]

# Add new row
df_merged.loc[len(df_merged.index)] = [29,3,3,1,1,3,3]

# delete last column
df_merged.drop(columns=df_merged.columns [6], axis= 1 , inplace= True)

# delete last row
df_merged.drop(labels=[12],axis=0,inplace=True)

# print data of sep
# print(df_merged['sep'])

# print staff, who have made > 43000 sales per month
print(df_merged.loc[(df_merged['nov'] >43000)])