from numpy.f2py.crackfortran import endifs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.syf.tw/"


def search_get_text(search_query):
    driver = webdriver.Chrome()


    try:
            driver.get(url)


            search_box = driver.find_element(By.ID, "header-search")
            search_box.send_keys(search_query)
            time.sleep(0.5)

            preview =  driver.find_element(By.XPATH,"//div[@class='predictive-result__info flex-auto']")
            preview_click = preview.click()
            time.sleep(1)

            item = driver.find_element(By.XPATH,"//div[@class='product-info__block product-info__block--sm "
                                                "product-info__title']//h1")
            item_name =  item.text.split('-')
            item_name = item_name[0]

            url_get = driver.current_url
            item_list = [search_query,item_name,url_get]

            goods_id = list()
            goods_name = list()
            goods_num = 0

            print(item_list)
    finally:
            driver.quit()




#輸入:
input_list = list()
input_list = input("輸入編號: ")

while True :
    for item in input_list:
        if item == "":
            break
            print("輸入為空")
        query = input_list
    break

search_get_text(query)


