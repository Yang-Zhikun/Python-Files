import os
import shutil
from pathlib import Path

def convert_gbk_to_utf8(root_dir):
    # 需要处理的文件扩展名
    target_extensions = ('.cpp', '.h')
    
    # 遍历目录下所有文件
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # 只处理目标文件类型
            if filename.lower().endswith(target_extensions):
                file_path = Path(dirpath) / filename
                try:
                    # 读取GBK编码文件
                    with open(file_path, 'r', encoding='gbk') as f:
                        content = f.read()
                    
                    # 创建备份文件
                    backup_path = file_path.with_suffix(f'{file_path.suffix}.bak')
                    shutil.copy2(file_path, backup_path)
                    
                    # 以UTF-8编码写入文件
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f'✅ 已转换: {file_path}')
                    print(f'   备份文件: {backup_path}\n')
                    
                except UnicodeDecodeError:
                    print(f'❌ 解码失败，可能不是GBK编码: {file_path}\n')
                except Exception as e:
                    print(f'❌ 处理失败 {file_path}: {str(e)}\n')

if __name__ == '__main__':
    # 设置项目根目录
    project_root = Path(__file__).parent
    print(f'开始批量转换GBK到UTF-8...')
    print(f'目标目录: {project_root}\n')
    
    # 执行转换
    convert_gbk_to_utf8(project_root)
    
    print('转换完成！')
    print('注意事项:')
    print('1. 所有原始文件已创建.bak备份')
    print('2. 解码失败的文件可能不是GBK编码或包含特殊字符')
    print('3. 转换完成后建议删除备份文件cmd中打开项目目录执行"del /s *.bak"（如确认转换无误）')