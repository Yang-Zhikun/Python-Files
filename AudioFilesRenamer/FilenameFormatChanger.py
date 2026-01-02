"""
文件名格式转换工具, 将文件名的 - 两端的内容互换
例如：将 "Artist - Title.mp3" 转换为 "Title - Artist.mp3", 或 "Title - Artist" 转换为 "Artist - Title"
用于批量修改音频文件的命名格式
"""
import os
# 选择文件夹
print("欢迎使用文件名格式转换工具")
print('将文件名"-"两端的内容互换,扩展名保持不变, 确保文件名只包含一个"-"')
print("***强烈建议在转换前备份文件夹中的文件！\n")
print("请将要转换的文件夹拖进来或输入路径: ")
dir_path: str = input()
# 去掉路径两端的双引号（如果有的话）
dir_path = dir_path.strip('"')
print()
# 扫描文件夹中的文件(不包含文件夹)并保存
scrFiles: list = []
for file in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file)):
        print(file)
        scrFiles.append(file)
print(f"\n**找到 {len(scrFiles)} 个文件。")
# 生成新文件名列表
print("\n文件名对照表:\n")
newFilenames: list = []
for file in scrFiles:
    if '-' not in file:
        newFilenames.append(file) # 不包含 "-" 的文件名保持不变
    else:
        name_part, ext = os.path.splitext(file)
        parts = name_part.split('-')
        if len(parts) != 2:
            newFilenames.append(file) # 包含多个 "-" 的文件名保持不变
        else:
            part1 = parts[0]
            part2 = parts[1]
            new_name = f"{part2}-{part1}{ext}"
            newFilenames.append(new_name)
# 打印文件名对照表
for i in range(len(scrFiles)):
    print(f"{i+1}:  {scrFiles[i]}  -->  {newFilenames[i]}")
# 确认并执行重命名
print("\n确认重命名吗？(y/n)")
confirm: str = input()
if confirm.lower() == 'y':
    for i in range(len(scrFiles)):
        os.rename(os.path.join(dir_path, scrFiles[i]), os.path.join(dir_path, newFilenames[i]))
    print("\n重命名完成！")
else:
    print("\n操作已取消。")