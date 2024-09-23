from playwright.sync_api import sync_playwright
import time
import playwright


def main(search_query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.google.com')

        # 等待页面完全加载
        page.wait_for_load_state('networkidle')

        # 等待搜索框元素可用
        search_box = page.locator('#APjFqb')

        if search_box:
            print("找到搜索框")
            search_box.fill(search_query)
            search_box.press('Enter')
        else:
            print("仍然没有找到搜索框")
            return

        syf_count = 0
        sponsor_ad_count = 0
        next_page_count = 0

        while next_page_count < 10:
            # 等待页面加载
            page.wait_for_load_state('networkidle')


            # 检查是否有 "贊助商廣告" 的标签
            ad_labels = page.query_selector_all('span:has-text("贊助商廣告")')
            sponsor_ad_count += len(ad_labels)
            print(f"页面 {next_page_count + 1} 发现 '贊助商廣告': {len(ad_labels)} 次")

            # 查找所有可能的 'syf' 关键字元素
            elements_with_syf = page.query_selector_all('span:has-text("syf")')

            for element in elements_with_syf:
                # 获取元素的父级元素，可能包含多个层次
                parent_elements = page.evaluate('''(element) => {
                    const parentDiv = element.closest("div");
                    return Array.from(parentDiv.querySelectorAll("a"));
                }''', element)

                # 检查链接是否包含特定网站
                is_excluded = False
                for link in parent_elements:
                    href = link.__getattribute__('href')
                    if href and 'syf.com.tw' in href:
                        is_excluded = True
                        break  # 只要找到一个链接包含特定网址就可以排除

                if not is_excluded:
                    # 给符合条件的元素标记红色边框
                    page.evaluate('''(element) => {
                        element.style.border = '3px solid red';
                    }''', element)
                    syf_count += 1
                    print(f"页面 {next_page_count + 1} 发现 'syf': {syf_count} 次")

            # 尝试找到“下一页”按钮并点击
            next_button = page.query_selector('a:has-text("下一頁")')
            if next_button:
                next_button.click()
                next_page_count += 1
            else:
                print("没有找到 '下一页' 按钮，停止爬取。")
                break

        print(f"总共发现 'syf': {syf_count} 次")
        print(f"总共发现 '贊助商廣告': {sponsor_ad_count} 次")
        browser.close()


if __name__ == "__main__":
    search_term = input("请输入搜索词：")
    main(search_term)
