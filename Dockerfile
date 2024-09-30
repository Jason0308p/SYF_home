# 使用官方 Python 基礎映像
FROM python:3.12

# 設置工作目錄
WORKDIR /app

# 複製 Python 腳本到容器中
COPY script.py .

# 設定容器啟動時執行的命令
CMD ["python", "script.py"]
