import pandas as pd
from pandas import read_excel

data  = read_excel(r"C:\Users\syf\Desktop\check.xlsx" ,engine='openpyxl' )

column1 = 'A'
column2 = 'B'

check_data = data[column1].equals(data[column2])

if check_data:
    print("相同")
    print(data[column1])
    print(data[column2])
else:
    print("不同")
