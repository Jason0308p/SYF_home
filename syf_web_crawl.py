from numpy.f2py.crackfortran import endifs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://www.syf.tw/"
def search_get_text(search_query):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        search_box = driver.find_element(By.ID, "header-search")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        goods_id = list()
        goods_name = list()
        goods_num = 0
    finally:
        driver.quit()
input_list = list()
input_list = input("輸入四個編號: ")

query = input_list.split()



