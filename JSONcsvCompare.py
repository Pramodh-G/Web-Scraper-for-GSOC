import pandas as pd
import re
import numpy as np

filecsv = input()
filejson = input()
df1 = pd.read_csv(filecsv,index_col=False)
df2 = pd.read_json(filejson)

df1 =df1[~(df1['Name'].str.match("^[a-z]+$"))] #removed names with all small letters
df1=df1[~(df1['Name'].str.match("^\b[a-zA-Z]+\b$"))] #removed names with only one word
df1=df1[(df1['Name'].str.match("^[a-zA-Z\s]*$"))] #removes names with special characters



data=[]
for i,name1 in enumerate(df1['Name']): 

  for j,name2 in enumerate(df2['n']):
    if(name1 == name2):
      data.append([name1,df2.iloc[j,5],df2.iloc[j,2],df1.iloc[i,1],df1.iloc[i,2]])

df = pd.DataFrame(data,columns=['Name','RollNo','Branch','Organization','Project']) 

print(df)

