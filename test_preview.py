from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # 可选，用于自动管理 ChromeDriver
import time

# 初始化 WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.syf.tw/')  # 替换为你的目标网址

search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header-search"))  # 替换为实际的搜索框选择器
)

search_box.send_keys('56KA-1010')  # 输入你的查询字符串

try:
    predictive_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
             (By.XPATH, '//div[contains(@class, "predictive-result__info") and contains(@class, "flex-auto")]'))
        )
    title_element = predictive_div.find_element(By.XPATH, "//div[@class='predictive-result__info flex-auto']//h3")
    title_text = title_element.text
    time.sleep(1)

    print("Extracted Title:", title_text)


finally:
    driver.quit()
