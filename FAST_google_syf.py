from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_and_scroll(search_query):
    # 设置 Chrome 驱动程序
    driver = webdriver.Chrome()

    try:
        # 打开 Google 首页
        driver.get("https://www.google.com")

        # 搜索框输入关键词并进行搜索
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "APjFqb"))
        )
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        next_page_count = 0    # 记录搜索页数
        sponsor_ad_count = 0   # 记录广告数量
        syf_count = 0          # 记录syf字符串出现次数(不含广告)

        while next_page_count < 10:
            # 等待页面加载
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )

            # 检查页面中是否有 "赞助商广告" 的标签
            ad_labels = driver.find_elements(By.XPATH, ".//span[contains(text(),'贊助商廣告')]")
            cite_elements = driver.find_elements(By.XPATH, "//cite[contains(text(), 'https://www.syf.com.tw')]")

            # 如果没有找到赞助商广告，才检查 syf
            if not ad_labels and not cite_elements:
                if "syf" in driver.page_source:
                    syf_count += 1
                    print(f"没有赞助商广告，目前在第{next_page_count + 1}页，出现了字符串 'syf'")
                    print(f"目前共累计{syf_count} 次'syf'")

                    # 找到包含 'syf' 字符串的元素
                    elements = driver.find_elements(By.XPATH, "//*[contains(text(),'syf')]")
                    for element in elements:
                        # 滚动到元素位置并加上红色边框
                        driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'})", element)
                        driver.execute_script("arguments[0].style.border='3px solid red'", element)
                        WebDriverWait(driver, 2).until(
                            EC.visibility_of(element)
                        )
                else:
                    print(f"目前在第{next_page_count+1}页， 'syf' 没有找到。")
            else:
                # 记录赞助商广告的数量
                sponsor_ad_count += len(ad_labels)
                print(f"这个页面出现{len(ad_labels)}个 '赞助商广告'，共累计{sponsor_ad_count}个广告")

            # 尝试找到“下一页”按钮并点击
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "pnnext"))
                )
                next_button.click()
                next_page_count += 1
            except Exception as e:
                print("无下一页")
                break

        print(f"共搜索{next_page_count}页")
        print(f"共找到了{syf_count}个syf关键字。")
        print(f"共找到了{sponsor_ad_count}个赞助商广告。")

    finally:
        driver.quit()

# 定义完函数后执行
if __name__ == "__main__":
    query = input("请输入搜索关键字: ")
    search_and_scroll(query)
