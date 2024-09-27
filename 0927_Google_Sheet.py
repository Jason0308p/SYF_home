import pygsheets
import pandas as pd

#授權
url = "C:/Users/syf/Desktop/code/data0923-a22f23dd44ce.json"
gc = pygsheets.authorize(service_file = url)

#讀取 "宜搭每日訂單"，並抓資料
sheet_url = "https://docs.google.com/spreadsheets/d/1w06m2DRUgfrxbGmYK4OwquNFHEkTq8bbx7JqVCzCUeU/edit"
sheet_name = gc.open_by_url(sheet_url)
sheets = sheet_name.worksheets()
data = sheets[0].get_values("A2","F400")

# 刪掉不要的欄位

#轉換成 dataframe ，然後對其中的欄位進行格式轉換，日期轉成:月、ISO週數
df = pd.DataFrame(data[1:],columns=data[0])
df = df.drop(columns = ['1.總訂單金額','1.環比上月增值','2.總訂單金額','2.環比上月增值'])
df.rename(columns = {"3.總訂單金額":"總訂單金額"},inplace=True)
df.columns = df.columns.str.strip()
df['日'] = pd.to_datetime(df['日'])
df['月'] = df['日'].dt.month
df['週'] = df['日'].dt.isocalendar().week

# gsheet數字有千分位逗號，，並且轉為數字格式
df['總訂單金額'] = df['總訂單金額'].str.replace(",","").astype(int)

# 依群組加總: groupby ，再進行排序
df_month = df.groupby('月')['總訂單金額'].sum().reset_index().sort_values(by="月",ascending=False)
df_week = df.groupby('週')['總訂單金額'].sum().reset_index().sort_values(by="週",ascending=False)


# 寫入 dataframe 資料，到 google sheet
sheets[1].set_dataframe(df_month, (1, 1))
sheets[2].set_dataframe(df_week, (1, 1))


#------------------------------------------ 其他功能 ----------------------------------------------
# 清除工作表資料
# clear_sheet = sheet_name.worksheet('title','test')
# clear_sheet.clear()

# 新增空白欄位
# add_row = sheet_name.worksheet('title','週資料')
# add_row.insert_rows(1,1,values=[],inherit=False)


# wks.update_value('C2', '=SUM(B2:B10)')
