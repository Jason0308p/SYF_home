import pygsheets
import pandas as pd

# 授權
url = "C:/Users/syf/Desktop/code/data0923-a22f23dd44ce.json"
gc = pygsheets.authorize(service_file=url)

# googel sheet 打開方式
# gc.open(名稱或URL)
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1z1eVTyEn3SLOyDeNqY2suDaBtwkZ9Wf2k55vHTVf36g/edit")

# 讀取工作表
sheets = sht.worksheets()
sheet1, sheet2, sheet3 = sheets[0], sheets[1], sheets[2]

# 抓取資料
df1 = pd.DataFrame(sheet1.get_all_values())
#print(df1.iloc[0])


result = df.groupby('类别')['金额'].sum().reset_index()

# 新增工作表
#new_sheet = spreadsheet.add_worksheet('NewSheet', rows=100, cols=26)
# 将 DataFrame 写入 Google Sheets，开始位置设为 A1
#sheet.set_dataframe(df, (1, 1))  # (1, 1) 代表 A1 单元格
# 读取 Google Sheets 中已有的数据，转换为 Pandas DataFrame
#existing_data = sheet.get_as_df()
# 创建一个新列，例如 "Country"
#existing_data['Country'] = ['USA', 'Canada', 'UK']  # 添加新列
# 将更新后的 DataFrame 写回 Google Sheets，覆盖旧数据
sheet.set_dataframe(existing_data, (1, 1))