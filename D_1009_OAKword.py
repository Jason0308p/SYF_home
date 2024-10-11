import re
import pygsheets
import pandas as pd

# 授权和打开Google Sheets
url = "C:/Users/syf/Desktop/code/data0923-a22f23dd44ce.json"
sheet_url = "https://docs.google.com/spreadsheets/d/18H9Qh64jqWMRNnv_-tLj85mkUCYAYjulTHqiHX7zrdk/edit"
gc = pygsheets.authorize(service_file=url)
sheet_location = gc.open_by_url(sheet_url)
sheets = sheet_location.worksheets()

# 获取数据
df = sheets[1].get_as_df(has_header=True)

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# 使用正则表达式提取每行中的所有中文短语
def extract_chinese_phrases(text):
    pattern = r'[\u4e00-\u9fa5]+'  # 匹配中文字符
    matches = re.findall(pattern, text)  # 查找所有匹配的中文短语
    return matches  # 返回中文短语列表

# 修改列名访问
df['chinese_phrases'] = df['OA關鍵字'].apply(extract_chinese_phrases)
df2 = df['chinese_phrases'].to_frame()

# 展平成一維 Dataframe:  .explode()
df_flat = df2.stack().explode().reset_index(drop=True).to_frame(name='關鍵字')

#
# sheet_location.add_worksheet('OA關鍵字')
# sheets[2].set_dataframe(df_flat,'A1')



