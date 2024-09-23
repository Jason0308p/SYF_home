from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 设置 Chrome 驱动器
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 打开网页
url = "https://c7bmuc.aliwork.com/APP_ISWDBE7PK4NM53UA7RPP/admin/FORM-0A966I81QCGCW3MS85WTZ3LIY8F63Y6IEW0KL6"
driver.get(url)

# 获取网页内容
web_content = driver.page_source

# 关闭浏览器
driver.quit()

# 解析网页内容
from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')

# 查找包含特定 class 的 span 标签
span_tag = soup.find('span', class_="Theme--rowTitle--3dT6u8",
                     attrs={"aria-haspopup": "true", "aria-expanded": "false"})

# 获取标签内的文字
if span_tag:
    text_content = span_tag.get_text()
    print(f"标签内容: {text_content}")
else:
    print("未找到匹配的标签")



##########################
import requests

# 目标网页的 URL
url = "你的目标网页链接"

# 发送 HTTP 请求并获取网页内容
response = requests.get(url)
web_content = response.text

# 打印网页内容的一部分
print(web_content[:2000])  # 打印前 2000 个字符
with open('webpage.html', 'w', encoding='utf-8') as file:
    file.write(web_content)