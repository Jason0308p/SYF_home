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

        next_page_count=0

        while next_page_count < 10 :
            # 等待頁面加載
            time.sleep(0.8)

            url_elements = driver.find_elements(By.XPATH, "//span[@class='VuuXrf' and contains(text(), 'syf.tw')]")

            if url_elements  :
                print(f" 'url_elements'為 {url_elements}")
                next_page_count += 1
            else:
                print("沒有找到")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.6)

        for element in url_elements:
            print(f"Found element with text: {element.text}")

    finally:
        driver.quit()

if __name__ == "__main__":
    query = input("請輸入搜尋關鍵字: ")
    search_and_scroll(query)