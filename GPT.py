import os
import openai
import tiktoken
import requests

encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")


# def num_tokens_from_string(string: str, encoding_name: str) -> int:
#   """Returns the number of tokens in a text string."""
#   encoding = tiktoken.get_encoding(encoding_name)
#   num_tokens = len(encoding.encode(string))
#   return num_tokens
# tokens_num = num_tokens_from_string("這是一段文字嗎? 哈 ㄏ", "cl100k_base")
# #print(tokens_num)


key = os.getenv("GPT_API_KEY")      #抓取環境變數
openai.api_key = key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-1106",  # 可以根据需要选择不同的模型
  messages=[
    {"role": "user", "content": "用20字說明API是什麼。"}
  ]
)
print(response)

