import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.syf.tw/"

def search_get_text(search_query):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 使用無頭模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.ID, "header-search")))
        search_box.clear()  # 清空輸入框
        search_box.send_keys(search_query)

        preview = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='predictive-result__info flex-auto']")))
        preview.click()

        item = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-info__block product-info__block--sm product-info__title']//h1")))
        item_name = item.text.split('-')[0]

#        img_url = wait.until(driver.find_element(By.XPATH, "//div[contains(class='media relative')]//a//picture//source"))


        url_get = driver.current_url
        item_list = [search_query, item_name, url_get]

        print(item_list)
    finally:
        driver.quit()

# 主程序
input_list = input("輸入編號 (用逗號分隔): ")
search_queries = [query.strip() for query in input_list.split(",") if query.strip()]

threads = []

for query in search_queries:
    thread = threading.Thread(target=search_get_text, args=(query,))
    threads.append(thread)
    thread.start()

# 等待所有線程完成
for thread in threads:
    thread.join()
