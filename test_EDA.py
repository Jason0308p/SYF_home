from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化 WebDriver
driver = webdriver.Chrome()  # 或使用你选择的其他 WebDriver
driver.get('https://c7bmuc.aliwork.com/APP_ISWDBE7PK4NM53UA7RPP/admin/FORM-0A966I81QCGCW3MS85WTZ3LIY8F63Y6IEW0KL6')

# 初始化 WebDriverWait
wait = WebDriverWait(driver, 10)  # 10 秒的等待时间

# 打开目标网站
try:
    # 等待元素存在且可点击
    phone_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'module-pass-login-type-tab-item')]"))
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'module-pass-login-type-tab-item module-pass-login-type-tab-item-active')]"))
    )
    phone_tab.click()

    # 等待并找到手机号码输入框
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='tel' and @placeholder='請輸入手機號碼']"))
    )
    phone_number = "0975671612"  # 替换为实际的手机号码
    phone_input.send_keys(phone_number)

except Exception as e:
    print(f"Error: {e}")



finally:
    time.sleep(3)  # 浏览器保持打开10秒



#     # 等待下拉选单并选择国家代码
#     country_code_dropdown = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//div[@class='country-code-dropdown']"))  # 替换为实际的下拉选单选择器
#     )
#     country_code_dropdown.click()
#
#     # 选择 +886 选项
#     country_code_option = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//div[@class='country-code-option' and text()='+886']"))
#         # 替换为实际的 +886 选项选择器
#     )
#     country_code_option.click()
#     print("已选择+886国家代码。")
#
#     # 输入手机号码
#     phone_number_input = wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//input[@name='phone-number']"))  # 替换为实际的手机号码输入框选择器
#     )
#     phone_number_input.send_keys('0975671612')
#     print("已输入手机号码。")
#
#     # 点击“下一步”按钮
#     next_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'next-button')]"))  # 替换为实际的“下一步”按钮选择器
#     )
#     next_button.click()
#     print("已点击'下一步'按钮。")
#
# except Exception as e:
#     print(f"发生错误: {e}")

# 关闭 WebDriver
driver.quit()
