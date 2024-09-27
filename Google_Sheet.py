import pygsheets
import pandas as pd
#---------------------------------------------------------------------------------------
# 授權

url = "C:/Users/syf/Desktop/code/data0923-a22f23dd44ce.json"
gc = pygsheets.authorize(service_file = url)

#---------------------------------------------------------------------------------------
# 讀取

# google sheet 打開方式
# gc.open(名稱或URL)
# 宜搭每日訂單_副本
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1z1eVTyEn3SLOyDeNqY2suDaBtwkZ9Wf2k55vHTVf36g/edit")

# 讀取工作表
sheets = sht.worksheets()
sheet1, sheet2, sheet3 = sheets[0], sheets[1], sheets[2]
# 讀取全部資料、部分資料
# data = sheet1.get_all_values()
data = sheet1.get_values("A1","F75")

#---------------------------------------------------------------------------------------
# 轉成 dataframe 並加工

# 將資料轉成 dataframe，因為第二行開始才是數據，第一行為欄位名稱
df = pd.DataFrame(data[1:],columns=data[0])
#print(df)

# 清除欄位前後空白
df.columns = df.columns.str.strip()

# 先將日期欄，转换为日期格式
df['日'] = pd.to_datetime(df['日'])

# 轉換成 ISO 周数
df['週'] = df['日'].dt.isocalendar().week
df_clean = df.dropna(subset=['週'])

# 输出單列為[]，輸出多列為[[]]
#print(df[["週","日"]])

# 先將金額轉成數字，並且去除逗號，例如十萬 100,000 改成100000
# str是一個屬性，，可提供pandas series中的每個字串進行訪問，replace則是字串的一個方法
df_clean["3.總訂單金額"] = df_clean["3.總訂單金額"].str.replace("," , "").astype(int)

# 依照"週"做分類群，相同的週，把其 3.總訂單金額，進行sum加總，再reset_index到原始的欄位 3.總訂單金額
df_group = df_clean.groupby("週")["3.總訂單金額"].sum().reset_index()
df_group["週訂單金額總和"] = df_group["3.總訂單金額"]
df_sorted = df_group.sort_values(by = "週" , ascending = False)

#---------------------------------------------------------------------------------------
# 新增欄位

add_row = sht.worksheet('title','test')
# append 會把資料新增到整個表的最下面一個資料
#add_row.append_table(['2024-09-20',115160,115160,45590,45590],start='A1',dimension='ROWS',overwrite=False)

# 新增 row data
# 但此新增無法代入公式，因此需另外計算好再帶入
add_row.insert_rows(1,2,values = [['2024-09-25', 26500, 26500, 26500],['2024-09-24', 222, 111, 1111]], inherit=False)


# 打印出每個sheet的索引，每個工作表有各自的index，再進行刪除該index的工作表
# print(sht.worksheets())
#sht.del_worksheet(sht.worksheets()[3])

# 新增工作表，並且將想放的資料，貼到新工作表，從A1開始(如同複製貼上報表)
#new_sheet = sht.add_worksheet("週-總訂單金額",rows = 80 ,cols = 80 )
#new_sheet.set_dataframe(df_sorted,"A1")
# print(new_sheet)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# 其他補充
#result = df1.groupby('類別')['金額'].sum().reset_index()
#result2 = df1.groupby('類別')['金額'].sum().transform("總金額")

# transform 可新增一個欄位，名稱為...
# reset_index()  把sum的結果重新加入到原有的index欄位

# 新增工作表
#new_sheet = spreadsheet.add_worksheet('NewSheet', rows=100, cols=26)
# 将 DataFrame 写入 Google Sheets，开始位置设为 A1
#sheet.set_dataframe(df, (1, 1))  # (1, 1) 代表 A1 单元格
# 读取 Google Sheets 中已有的数据，转换为 Pandas DataFrame
#existing_data = sheet.get_as_df()
# 创建一个新列，例如 "Country"
#existing_data['Country'] = ['USA', 'Canada', 'UK']  # 添加新列

# 将更新后的 DataFrame 写回 Google Sheets，覆盖旧数据
#sheet.set_dataframe(existing_data, (1, 1))
# 新增/更新儲存格
#wks.update_value('A1', 'test')
# 以dataframe形式寫入資料
#df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
#wks.set_dataframe(df1, 'A2', copy_index=True, nan='')

#new_sheet = sht.add_worksheet(title='test',rows=20,cols=20)

