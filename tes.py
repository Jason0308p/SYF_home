from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置 WebDriver
service = Service(executable_path='path/to/chromedriver')
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 如果需要在无界面模式下运行
driver = webdriver.Chrome(service=service, options=chrome_options)
url="https://login.dingtalk.com/oauth2/challenge.htm?redirect_uri=https%3A%2F%2Fc7bmuc.aliwork.com%2Fdingtalk_sso_call_back%3Fcontinue%3Dhttps%253A%252F%252Fc7bmuc.aliwork.com%252FAPP_ISWDBE7PK4NM53UA7RPP%252Fadmin%252FFORM-GC9664C14RWA37EW8YQZ37FHZUTK26ANL61IL8&response_type=code&client_id=suite9xvlxxerybljwheo&scope=openid+corpid"

try:
    driver.get(url)

    # 等待并找到 "手机" 元素
    phone_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '手机')]"))
    )

    # 打印元素的 HTML，以检查是否可以点击
    print(phone_tab.get_attribute("outerHTML"))

    # 尝试点击元素
    try:
        phone_tab.click()
        print("点击成功")
    except Exception as e:
        print(f"点击失败: {e}")

finally:
    driver.quit()  # 关闭浏览器

















