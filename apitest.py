import requests
import datetime
url = "https://60s.viki.moe/v2/bing?encoding=json"

# 发送API请求
response = requests.get(url)
jsonData = response.json()  # 解析JSON响应
print(jsonData)

# 提取图片URL和版权信息
image_url = jsonData["data"]["cover"]

# 生成文件名,使用当前日期
date_str = datetime.datetime.now().strftime("%Y-%m-%d")
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
    print("请检查网络连接或API服务是否正常。")
