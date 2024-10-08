from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pygsheets
import pandas as pd

def search_and_scroll(search_query):
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(15)

        next_page_count = 0
        sponsor_ad_count = 0
        syf_data = []

        while next_page_count < 10:
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
    # 用於存儲每個查詢的結果
    results = {
        '廣告數量': [],
        'SYF網址': [],
        '頁數': [],
        'Google搜尋頁面URL': []
    }

    for index, query in enumerate(search_queries, start=1):
        print(f"\n----- 開始查詢第 {index} 個關鍵字: {query} -----\n")
        sponsor_ad_count, syf_data = search_and_scroll(query)

        # 如果 syf 出現的資料為空，則填充 None
        if syf_data:
            for entry in syf_data:
                results['廣告數量'].append(sponsor_ad_count)
                results['SYF網址'].append(entry['syf_url'])
                results['頁數'].append(entry['page'])
                results['Google搜尋頁面URL'].append(entry['google_search_page_url'])
        else:
            results['廣告數量'].append(sponsor_ad_count)
            results['SYF網址']
            results['頁數']
            results['Google搜尋頁面URL']

    # 將結果轉換為 DataFrame
    df = pd.DataFrame(results)
    return df

url = "C:/Users/syf/Desktop/code/data0923-a22f23dd44ce.json"
sheet_url = "https://docs.google.com/spreadsheets/d/18H9Qh64jqWMRNnv_-tLj85mkUCYAYjulTHqiHX7zrdk/edit"

def read_queries_from_google_sheet(sheet_name):
    gc = pygsheets.authorize(service_file=url)
    sheet_name = gc.open_by_url(sheet_url)
    sheets = sheet_name.worksheets()
    query_data = sheets[0].get_values("A2", "A10")
    queries = [row[0] for row in query_data]
    return queries

if __name__ == "__main__":
    queries = read_queries_from_google_sheet(sheet_url)
    final_df = batch_search(queries)
    print("\n----- 最終結果 -----")
    print(final_df.iloc[0])

gc = pygsheets.authorize(service_file=url)
sheet_name = gc.open_by_url(sheet_url)
sheets = sheet_name.worksheets()
sheets[0].insert_cols(col=2,number=len(final_df),values=final_df)