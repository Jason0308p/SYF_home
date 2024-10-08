import re
import pygsheets
import pandas as pd

# 授权和打开Google Sheets
url = "C:/Users/syf/Desktop/code/data0923-a22f23dd44ce.json"
sheet_url = "https://docs.google.com/spreadsheets/d/18H9Qh64jqWMRNnv_-tLj85mkUCYAYjulTHqiHX7zrdk/edit"
gc = pygsheets.authorize(service_file=url)
sheet_name = gc.open_by_url(sheet_url)
sheets = sheet_name.worksheets()

# 获取数据
data = sheets[1].get_values("A2", "A560")

# 将二维列表转换为单一字符串
data_string = ''.join([''.join(row) for row in data])

# 使用正则表达式提取所有中文字符
pattern = r'[\u4e00-\u9fa5]+'
matches = re.findall(pattern, data_string)

# 将提取结果转换为DataFrame，以便插入到工作表
df = pd.DataFrame(matches)

# 在第二列插入提取的中文字符
sheets[1].insert_cols(col=2, number=len(df), values=df.values.tolist())

print("提取的中文字符:", matches)
