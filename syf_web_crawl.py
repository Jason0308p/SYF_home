from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "https://www.syf.tw/"


def search_get_text(search_query):
    driver = webdriver.Chrome()


    try:
            driver.get(url)


            search_box = driver.find_element(By.ID, "header-search")
            search_box.send_keys(search_query)
            time.sleep(0.9)

            preview =  driver.find_element(By.XPATH,"//div[@class='predictive-result__info flex-auto']")
            preview.click()
            time.sleep(0.7)

            item = driver.find_element(By.XPATH,"//div[@class='product-info__block product-info__block--sm "
                                                "product-info__title']//h1")
            item_name =  item.text.split('-')
            item_name = item_name[0]

            url_get = driver.current_url
            item_list = [search_query,item_name,url_get]

            print(item_list)
    finally:
            driver.quit()

input_list = input("輸入編號 (用逗號分隔): ")

search_queries = [query.strip() for query in input_list.split(",") if query.strip()]

for query in search_queries:
    search_get_text(query)


