from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pygsheets
import pandas as pd
import numpy as np


def search_and_scroll(search_query):
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        #time.sleep(15)

        next_page_count = 0
        sponsor_ad_count = 0
        syf_data = []

        while next_page_count < 2:
        #while next_page_count < 10:
            time.sleep(1)

            current_page_url = driver.current_url

            ad_label = driver.find_elements(By.XPATH, ".//span[contains(text(),'贊助商廣告')]")
            sponsor_ad_count += len(ad_label)

            url_elements = driver.find_elements(By.XPATH, ".//cite[@role='text' and contains(text(),  'syf.tw')]")
            for element in url_elements:
                syf_data.append({
                    'syf_url': element.text,
                    'page': next_page_count + 1,
                    'google_search_page_url': current_page_url
                })

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.6)

            try:
                next_button = driver.find_element(By.ID, "pnnext")
                next_button.click()
                next_page_count += 1
            except Exception as e:
                break

        return sponsor_ad_count, syf_data

    finally:
        driver.quit()

def batch_search(search_queries):
    results = []  # 用于存储所有查询的结果

    for index, query in enumerate(search_queries, start=1):
        print(f"\n----- 开始查询第 {index} 个关键字: {query} -----\n")
        sponsor_ad_count, syf_data = search_and_scroll(query)

        found = False  # 确保每次循环开始时都初始化

        if syf_data:
            for entry in syf_data:
                if not found:  # 如果还没找到有效的 URL
                    results.append([  # 使用列表来存储每个查询的结果
                        sponsor_ad_count,  # 广告数量
                        entry['syf_url'],  # SYF网址
                        entry['page'],      # 页数
                        entry['google_search_page_url']  # Google 搜索页面 URL
                    ])
                    found = True  # 找到第一个有效的 SYF URL，标志位置为 True

        # 如果没有找到有效的 syf URL，仍然记录广告数量
        if not found:
            results.append([
                sponsor_ad_count,
                None,              # 填充 None
                None,              # 填充 None
                None               # 填充 None
            ])

    return results  # 返回包含子列表的列表，每个子列表表示一个查询的结果


# google sheet  操作
url = "C:/Users/syf/Desktop/code/data0923-a22f23dd44ce.json"
sheet_url = "https://docs.google.com/spreadsheets/d/18H9Qh64jqWMRNnv_-tLj85mkUCYAYjulTHqiHX7zrdk/edit"

gc = pygsheets.authorize(service_file=url)
sheet_name = gc.open_by_url(sheet_url)
sheets = sheet_name.worksheets()
query_data = sheets[0].get_values("A2", "A10")
queries = [row[0] for row in query_data]



if __name__ == "__main__":
    final_results = batch_search(queries)
    df = pd.DataFrame(final_results, columns=['广告数量', 'SYF网址', '页数', 'Google 搜索页面 URL'])

    # 重要!!! 把dataframe資料為 nan 轉換成 None，因為google sheet 只讀得懂None
    #df = df.where(pd.notnull(df),None)
    print("DataFrame before converting to list:")
    print(df)


    data_with_headers = [df.columns.tolist()] + df.values.tolist()
    data_to_insert = df.values.tolist()


    pd.set_option('display.max_rows',None)
    pd.set_option('display.max_columns',None)

    # 這段 update方式很實用
    # update_row 第一個參數為index，為輸入的row number
    # col_offset 為跳過幾個col後再輸入資料
    for number in range(len(data_to_insert)):
        num = number+2

        # 重要!!!
        # 再次確保倒入 google sheet 時沒有nan
        data_to_insert[number] = [None if pd.isna(x) else x for x in data_to_insert[number]]
        sheets[0].update_row(num, values=data_to_insert[number],col_offset=1)

    print("\n----- 最終結果 -----")
    print(df)

