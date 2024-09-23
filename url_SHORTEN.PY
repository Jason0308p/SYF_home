from bitlyshortener import Shortener
import os

# 从环境变量获取 Bitly API token
test_key = os.getenv('Bitly_API_token')

# 确保 API token 被正确设置并且是一个列表
if test_key is None:
    raise ValueError("Bitly API token not found. Please set the 'Bitly_API_token' environment variable.")

# 创建 Shortener 物件
shortener = Shortener(tokens=[test_key])  # 将 API token 放入列表中

# 需要缩短的 URL
long_url1 = "https://www.syf.tw/collections/%E6%97%A5%E8%AA%8C%E7%AD%86%E8%A8%98/products/54ea-0101"
long_url2 = "https://www.syf.tw/products/64ea-0918"
long_url3= ("https://www.facebook.com/syfgifts/posts"
            "/pfbid0ijR1fV4mm1xy1a14WqQ4ztXDPhqTzWqtAp9A4uyUgrGajf8aFc31Yc1ViWrKYy43l"
    "?locale=zh_TW")

# 缩短 URL
short_url = shortener.shorten_urls([long_url3])[0]
print(short_url)
