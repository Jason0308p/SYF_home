from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def search_and_scroll(search_query):
    # 設置 Chrome 驅動程式
    driver = webdriver.Chrome()

    try:
        # 打開 Google 首頁
        driver.get("https://www.google.com")

        # 搜尋框輸入關鍵字並進行搜尋
        search_box = driver.find_element(By.ID, "APjFqb")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        next_page_count = 0    # 紀錄搜尋頁數
        sponsor_ad_count = 0   # 紀錄廣告數量
        syf_count = 0          # 紀錄syf字串出現次數(不含廣告)


        while next_page_count < 10 :
            # 等待頁面加載
            time.sleep(1)

            # 檢查頁面中是否有 "贊助商廣告" 的標籤
            ad_label = driver.find_elements(By.XPATH, ".//span[contains(text(),'贊助商廣告')]")
            cite_element = driver.find_elements(By.XPATH, ".//cite[@role='text' and contains(text(), 'https://www.syf.com.tw')]")


            # 如果沒有找到贊助商廣告，才檢查 syf
            if not ad_label and not cite_element:
                url_elements = driver.find_elements(By.XPATH, ".//cite[@role='text' and contains(text(),  'syf.tw')]")
                for element in url_elements:
                    print(f"Element text: {element.text}")

                    if "syf.tw" in element.text:

                        driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'})",
                                              element)
                        driver.execute_script("arguments[0].style.border='3px solid red'", element)
                        time.sleep(1.8)

                        print(f" 測試  {url_elements}")
                        syf_count += 1
                        print(f"沒有贊助商廣告，目前在第{next_page_count + 1}頁，出現了字串 'syf'")
                        print(f"目前共累積{syf_count} 次'syf'")


                    else:
                        print(f"目前在第{next_page_count+1}頁， 'syf' 沒有找到。")
            else:
                # 記錄贊助商廣告的數量
                sponsor_ad_count += len(ad_label)
                print(f"目前在第{next_page_count + 1}頁， 'syf' 沒有找到。")
                print(f"這個頁面出現{len(ad_label)}個 '贊助商廣告'，共累積{sponsor_ad_count}個廣告")


            # 瀏覽器滑動至底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.6)

            # 找到 "下一頁" 的按鈕並點擊
            try:
                next_button = driver.find_element(By.ID, "pnnext")
                next_button.click()
                next_page_count += 1
            except Exception as e:
                print("無下一頁")
                break
        print(f"共搜索{next_page_count}頁: {search_query} ")
        print(f"共找到了{syf_count}個syf關鍵字。")
        print(f"共找到了{sponsor_ad_count}個贊助商廣告。")

    finally:
        driver.quit()



# 定義完函數後執行
if __name__ == "__main__":
    query = input("請輸入搜尋關鍵字: ")
    search_and_scroll(query)
