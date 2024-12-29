import os

def process_and_save_lrc_file(file_path):
    # 读取文件内容，并处理可能的编码问题
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:  # 使用'utf-8-sig'自动处理BOM
            lines = file.readlines()
    except UnicodeDecodeError:
        # 如果文件不是UTF-8编码，可以尝试其他编码，或者使用'ignore'或'replace'错误处理
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()

    # 删除以特定字符串开头的行
    lines_to_keep = []
    for line in lines:
        if not line.startswith('[ti:新概念英语第二册]') and not line.startswith('[by:http://www.TingClass.com]') and not line.startswith('[ti:¸Ӣڶ]') and not line.startswith('\n'):
            lines_to_keep.append(line)

    # 替换"&#39;"为"'"
    processed_lines = [line.replace("&#39;", "'") for line in lines_to_keep]

    # 以UTF-8编码（不带BOM）的形式写回文件
    with open(file_path, 'w', encoding='utf-8') as file:  # 默认不写BOM
        file.writelines(processed_lines)


def main(directory):
    # 遍历指定目录下的1.lrc到96.lrc
    for lesson_num in range(1, 97):
        filename = f"{lesson_num}.lrc"
        file_path = os.path.join(directory, filename)
        process_and_save_lrc_file(file_path)
        print(f"Processed and saved {file_path} as UTF-8")



if __name__ == "__main__":
    # 请将下面的路径替换为您要处理的文件夹的路径
    directory_path = "D:\听力\.新概念\新概念2"
    main(directory_path)
