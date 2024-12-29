#自动下载脚本
import requests as rq

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}


lesson_num = 1
file_folder = "G:/新概念2/"
print("保存路径：", file_folder)

fail_mp3s = []
fail_lrcs = []

for _ in range(1, 97): # 一共96课

    url_mp3 = "https://online1.tingclass.net/lesson/shi0529/0000/44/{}.mp3".format(lesson_num)
    url_lrc = "https://down11.tingclass.net/textrar/lesson/0000/44/{}.lrc".format(lesson_num)

    #下载mp3文件
    response = rq.get(url_mp3, headers=headers)
    if response.status_code == 200:
        with open(file_folder+"{}.mp3".format(lesson_num), mode="wb") as f:
            f.write(response.content)
            print("{}.mp3下载完成".format(lesson_num))
    else:
        print("{}.mp3下载失败".format(lesson_num))
        fail_mp3s.append(lesson_num)
        
        

    #下载lrc文件
    response = rq.get(url_lrc, headers=headers)
    if response.status_code == 200:
        with open(file_folder+"{}.lrc".format(lesson_num), mode="wb") as f:
            f.write(response.content)
            print("{}.lrc下载完成".format(lesson_num))
    else:
        print("{}.lrc下载失败".format(lesson_num))
        fail_lrcs.append(lesson_num)
    
    lesson_num += 1

print("下载失败的MP3：", fail_mp3s)
print("下载失败的LRC：", fail_lrcs)

print("保存路径：", file_folder)