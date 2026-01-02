"""
MusicFree音频文件批量重命名工具(命令行版)
请确保文件名的格式为：来源@ID@标题@艺术家
如：元力KG@1399346fjhfa@夜空中最亮的星@逃跑计划.mp3
"""

import os
class MusicFreeFileRenamer:
    # 支持的音频文件扩展名
    AUDIO_EXTENSIONS: tuple = ('.mp3', '.wav', '.flac', '.m4a', '.ogg', '.wma', '.aac')
    # 源文件列表
    src_filenames: list = []
    # 新文件名列表
    new_filenames: list = []
    # 重命名格式 0表示不重命名，1表示"标题-艺术家"，2表示"艺术家-标题"
    rename_format: int = 0

    def __init__(self):
        print("欢迎使用MusicFree旧版音频文件批量重命名工具(命令行版)")
        print("支持的音频文件扩展名: " + ", ".join(self.AUDIO_EXTENSIONS))
        print("注意：请确保文件名的格式为: 来源@ID@标题@艺术家")
        print("      如: 元力KG@1399346fjhfa@夜空中最亮的星@逃跑计划.mp3")
        print("      **强烈建议重命名前备份原文件！**\n")
        print("请将要重命名的音频文件夹拖进来或输入路径: ")
        self.dir_path: str = input()

        # 扫描文件夹中的音频文件并保存到源文件列表
        self.scanFiles(self.dir_path)
        
        # 选择重命名格式
        self.chooseRenameFormat()
        if self.rename_format == 0:
            print("程序结束。")
            return
        
        # 生成新文件名列表, 并保存到新文件名列表
        self.generateFilenames()

        # 打印文件名对照表并确认是否重命名
        if self.printRenameTable() == False:
            return

        # 重命名
        self.renameFiles()
        


    def scanFiles(self, dir_path):
        # 扫描文件夹中的音频文件并保存到源文件列表
        for filename in os.listdir(dir_path):
            if filename.lower().endswith(self.AUDIO_EXTENSIONS):
                self.src_filenames.append(filename)
                print(filename)
        print(f"\n**找到 {len(self.src_filenames)} 个音频文件。")

    def chooseRenameFormat(self):
        # 选择重命名格式
        print("**请选择重命名格式:")
        print("(0)不重命名")
        print("(1)标题-艺术家")
        print("(2)艺术家-标题")
        while True:
            choice = input("请输入选项编号(0/1/2): ")
            if choice in ('0', '1', '2'):
                self.rename_format = int(choice)
                break
            else:
                print("无效输入，请重新输入。")

    def generateFilenames(self):
        # 生成新文件名列表，原格式：来源@ID@标题@艺术家.扩展名, 并保存到新文件名列表
        for filename in self.src_filenames:
            parts = filename.split('@') # 以@分割文件名 为 来源、ID、标题、艺术家.扩展名 4个部分
            if len(parts) != 4:
                print(f"跳过文件(格式不正确): {filename}")
                self.new_filenames.append(filename)
                continue
            title = parts[2] # 标题
            extension = parts[3].split('.')[-1] # 扩展名 取最后一个点后的部分，防止标题或艺术家中有点
            ### 艺术家 取第3部分去掉扩展名
            artist = '.'.join(parts[3].split('.')[:-1])
            
            # 第一种重命名格式: 标题-艺术家
            if self.rename_format == 1:
                self.new_filenames.append(f"{title}-{artist}.{extension}")
            
            # 第二种重命名格式: 艺术家-标题
            elif self.rename_format == 2:
                self.new_filenames.append(f"{artist}-{title}.{extension}")
            
    def printRenameTable(self):
        # 打印文件名对照表并确认是否重命名
        print("\n**文件名对照表:")
        for i in range(len(self.src_filenames)):
            print(f"{i+1}:  {self.src_filenames[i]}  -->  {self.new_filenames[i]}")
        print("\n**是否确认重命名？(y/n): ")
        while True:
            choice = input()
            if choice in ('y', 'n'):
                break
            else:
                print("无效输入，请重新输入。")
        
        # 确认重命名
        if choice == 'y':
            return True
        else:
            print("程序结束。")
            return False
        
    def renameFiles(self):
        # 重命名文件
        self.fail_list = [] # 重命名失败列表
        for i in range(len(self.src_filenames)):
            src = os.path.join(self.dir_path, self.src_filenames[i])
            dst = os.path.join(self.dir_path, self.new_filenames[i])
            try:
                os.rename(src, dst)
                print(f"重命名成功: {self.src_filenames[i]}  -->  {self.new_filenames[i]}")
            except Exception as e:
                print(f"重命名失败: {self.src_filenames[i]}  -->  {self.new_filenames[i]}，错误: {e}")
                self.fail_list.append(self.src_filenames[i]) # 加入失败列表
        print(f"\n**重命名完成, 共{len(self.src_filenames)}个文件, 成功 {len(self.src_filenames)-len(self.fail_list)} 个, 失败 {len(self.fail_list)} 个文件。")
        if len(self.fail_list) > 0:
            print("\n**重命名失败的文件列表:")
            for filename in self.fail_list:
                print(filename)
            print("具体错误请参考上方提示。")


        
    



if __name__ == '__main__':
    r = MusicFreeFileRenamer()