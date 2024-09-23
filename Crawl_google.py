# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def search_and_scroll(search_query):
    # 使用 Chrome 驱动
    driver = webdriver.Chrome()

    try:
        # 打开 Google 首页
        driver.get("https://www.google.com")

        # 输入搜索查询
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        #time.sleep(14)

        next_page_count = 0   #紀錄搜尋頁數
        sponsor_ad_count = 0  #紀錄廣告數量
        syf_count = 0

        while next_page_count < 10:
            time.sleep(1.2)

            # 获取页面源码
            page_source = driver.page_source

            # 检查页面内容是否包含 "syf"
            if "syf" in page_source:

                #ad_label = driver.find_elements(By.XPATH, ".//span[contains(text(),'贊助商廣告')]")
                #cite_element = driver.find_elements(By.XPATH,".//cite[@role='text' and contains(text(), 'https://www.syf.com.tw')]")

                # 找到包含 'syf' 的元素
                url_elements = driver.find_elements(By.XPATH, ".//cite[@role='text' and contains(text(), 'syf.tw')]")
                if url_elements:

                        for element in url_elements:
                            # 滚动到元素位置
                            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",element)
                            # 给元素添加红色边框
                            driver.execute_script("arguments[0].style.border='3px solid red'", element)
                            syf_count += 1
                            print(f"'syf'出現在第{next_page_count+1}頁 ，共累積 {syf_count/2} ****** ")
                            time.sleep(1.5)


            #紀錄贊助商廣告數量
            sponsor_ads = driver.find_elements(By.XPATH,"//*[contains(text(), '贊助商廣告')]")
            sponsor_ad_count += len(sponsor_ads)
            # 输出当前页面找到的 "贊助商廣告" 数量
            print(f"第 {next_page_count+1}頁 沒找到'syf' ")
            print(f" 第 {next_page_count+1} 頁， '贊助商廣告'. 共累積: {sponsor_ad_count}")

            #加綠色邊框
            for ad in sponsor_ads:
                 driver.execute_script("arguments[0].style.border='3px solid green'", ad)

            # 滑动到页面底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 等待页面加载完成
            time.sleep(1.2)

            # 尝试找到并点击“下一页”按钮
            try:
                next_button = driver.find_element(By.ID, "pnnext")
                next_button.click()
                next_page_count += 1
            except Exception as e:
                print("无法找到下一页按钮，可能已到达最后一页。")
                break

        syf_count = syf_count/2
        syf_count = int(syf_count)
        print("---------------------------")
        print(f"查詢: {search_query} : ")
        print(f"共查詢 {next_page_count} 次下一页。")
        print(f"共找到 {sponsor_ad_count} 個'贊助商廣告'。")
        print(f"共找到 {syf_count} 個'syf'。 ")


    finally:
      driver.quit()

if __name__ == "__main__":
    query = input("请输入搜索内容: ")
    search_and_scroll(query)
