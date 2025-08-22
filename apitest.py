import requests
import json
from datetime import datetime

url = "https://60s.viki.moe/v2/bing?encoding=json"

# 发送API请求
response = requests.get(url)
data = response.json()  # 解析JSON响应

# 提取图片URL和版权信息
image_url = data["data"]["cover"]
#copyright = data["data"]["copyright"]

# 生成文件名（使用日期和版权信息）
raw_date = data["data"]["update_date"]  # "2025/08/18"
date_str = raw_date.replace("/", "")
#clean_copyright = "".join(x for x in copyright if x.isalnum() or x in " -_")[:30]  # 清理特殊字符
filename = f"{date_str}.jpg"

# 下载图片
image_response = requests.get(image_url, stream=True)
if image_response.status_code == 200:
    with open(filename, 'wb') as f:
        for chunk in image_response.iter_content(1024):
            f.write(chunk)
        print(f"图片已保存为: {filename}")
else:
    print(f"图片下载失败，状态码: {image_response.status_code}")