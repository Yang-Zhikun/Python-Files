"""
音频文件批量重命名工具
功能：批量重命名音频文件，支持自定义文件名格式和顺序，仅从文件名中解析信息
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class AudioFilesRenamer:
    """音频文件批量重命名工具类"""
    
    # 支持的音频文件扩展名
    AUDIO_EXTENSIONS = ('.mp3', '.wav', '.flac', '.m4a', '.ogg', '.wma', '.aac')
    
    # 非法文件名字符
    ILLEGAL_CHARS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    
    def __init__(self, width: int, height: int)-> None:
        """
        初始化应用程序
        
        Args:
            width: 窗口宽度
            height: 窗口高度
        """
        # 窗口基本设置
        self.root = tk.Tk()
        self.root.title('音频文件批量重命名工具')
        self.root.geometry(f'{width}x{height}')
        
        # 数据存储
        self.source_files = []  # 源文件列表
        self.preview_files = []  # 预览文件列表
        self.dir_path = ''  # 选择的文件夹路径
        self.rename_rule = None  # 重命名规则
        
        # 初始化UI
        self._init_ui()
        
        # 进入主循环
        self.root.mainloop()
    
    def _init_ui(self)-> None:
        """初始化用户界面"""
        # 初始化顶部按钮区
        self._init_buttons()
        
        # 创建主内容区域框架
        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 初始化左侧源文件列表
        self._init_source_list() 
        
        # 竖直分割线
        separator = tk.Frame(self.content_frame, width=2, bg="#cccccc")
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # 初始化右侧预览文件列表
        self._init_preview_list()
    
    def _init_buttons(self)-> None:
        """初始化顶部按钮区"""
        # 创建顶部按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, pady=10)
        
        # 创建按钮并添加到框架
        buttons = [
            ('选择文件夹', self.choose_directory),
            ('创建命名规则', self.create_rename_rule),
            ('文件名预览', self.preview_rename),
            ('重命名', self.rename_files),
            ('退出', self.root.quit)
        ]
        
        # 遍历创建按钮并设置布局
        for text, command in buttons:
            btn = tk.Button(
                button_frame, 
                text=text, 
                width=15, 
                height=2, 
                command=command
            )
            btn.pack(side=tk.LEFT, padx=5)
        
        # 设置框架居中
        button_frame.pack_configure(anchor=tk.CENTER)
        
        # 在按钮下方画一条水平分割线
        separator = tk.Frame(self.root, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)
    
    def _init_source_list(self)-> None:
        """初始化左侧源文件列表"""
        # 左侧源文件区域的框架
        self.source_frame = tk.Frame(self.content_frame)
        self.source_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 顶部标签
        self.source_label = tk.Label(self.source_frame, text=f"源文件列表    文件数量: {len(self.source_files)}")
        self.source_label.pack(pady=5)
        
        # 文件列表区域
        self.source_listbox = tk.Listbox(self.source_frame)
        self.source_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def _init_preview_list(self)-> None:
        """初始化右侧预览文件列表"""
        # 右侧预览区域
        self.preview_frame = tk.Frame(self.content_frame)
        self.preview_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 顶部标签
        self.preview_label = tk.Label(self.preview_frame, text=f"预览文件名列表    文件数量: {len(self.preview_files)}")
        self.preview_label.pack(pady=5)
        
        # 文件列表区域
        self.preview_listbox = tk.Listbox(self.preview_frame)
        self.preview_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def choose_directory(self)-> None:
        """选择文件夹，加载音频文件"""
        # 弹出文件夹选择框
        directory = filedialog.askdirectory(title="选择音频文件夹", initialdir=os.getcwd())
        
        if directory:
            self.dir_path = directory
            self._load_audio_files()
    
    def _load_audio_files(self)-> None:
        """加载并显示音频文件列表"""
        # 清空列表
        self.source_listbox.delete(0, tk.END)
        self.source_files.clear()
        
        try:
            # 扫描文件夹并筛选音频文件
            for filename in os.listdir(self.dir_path):
                if filename.lower().endswith(self.AUDIO_EXTENSIONS):
                    # 添加到源文件列表
                    self.source_listbox.insert(tk.END, filename)
                    self.source_files.append(filename)
            
            # 更新文件数量显示
            self.source_label.config(text=f"源文件列表    文件数量: {len(self.source_files)}")
            
            # 清空预览列表
            self._clear_preview_list()
            
        except Exception as e:
            messagebox.showerror("错误", f"加载文件失败: {str(e)}")
    
    def _clear_preview_list(self)-> None:
        """清空预览列表"""
        self.preview_listbox.delete(0, tk.END)
        self.preview_files.clear()
        self.preview_label.config(text=f"预览文件名列表    文件数量: 0")
    
    def create_rename_rule(self)-> None:
        """创建命名规则对话框"""
        self.rule_window = tk.Toplevel(self.root)
        self.rule_window.title("创建命名规则")
        self.rule_window.geometry("600x500")
        self.rule_window.resizable(True, True)
        
        # 创建三栏布局
        self._create_rule_window_layout()
    
    def _create_rule_window_layout(self)-> None:
        """创建命名规则窗口的布局"""
        # 左侧：可选项目
        left_frame = tk.Frame(self.rule_window)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(left_frame, text="可用选项", font=('Arial', 12, 'bold')).pack(pady=5)
        
        # 规则选项
        self.rule_options = {
            '艺术家': tk.BooleanVar(value=False),
            '标题': tk.BooleanVar(value=False),
            '来源': tk.BooleanVar(value=False),
            'ID': tk.BooleanVar(value=False)
        }
        
        # 创建复选框
        for key, var in self.rule_options.items():
            checkbox = tk.Checkbutton(left_frame, text=key, variable=var)
            checkbox.pack(anchor=tk.W, pady=3)
        
        # 中间：操作按钮
        center_frame = tk.Frame(self.rule_window)
        center_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=10)
        
        tk.Button(center_frame, text="添加 >", command=self._add_to_order).pack(pady=5)
        tk.Button(center_frame, text="< 移除", command=self._remove_from_order).pack(pady=5)
        tk.Button(center_frame, text="↑ 上移", command=self._move_up).pack(pady=5)
        tk.Button(center_frame, text="↓ 下移", command=self._move_down).pack(pady=5)
        
        # 右侧：顺序列表
        right_frame = tk.Frame(self.rule_window)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(right_frame, text="文件名顺序", font=('Arial', 12, 'bold')).pack(pady=5)
        
        self.order_listbox = tk.Listbox(right_frame, width=25, height=15)
        self.order_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # 保存按钮
        save_frame = tk.Frame(self.rule_window)
        save_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
        save_btn = tk.Button(save_frame, text="保存规则", command=self._save_rename_rule, width=20, height=2)
        save_btn.pack()

        # 初始化顺序列表
        self.selected_order = []
    
    def _add_to_order(self):
        """添加选中的选项到顺序列表"""     
        for key, var in self.rule_options.items():
            if var.get() and key not in self.selected_order:
                self.selected_order.append(key)
                self.order_listbox.insert(tk.END, key)
                break
    
    def _remove_from_order(self):
        """从顺序列表中移除选中的项"""
        selection = self.order_listbox.curselection()
        if selection:
            index = selection[0]
            removed = self.selected_order.pop(index)
            self.order_listbox.delete(index)
            # 取消对应的复选框选中状态
            if removed in self.rule_options:
                self.rule_options[removed].set(False)
    
    def _move_up(self):
        """将选中的项上移"""
        selection = self.order_listbox.curselection()
        if selection and selection[0] > 0:
            index = selection[0]
            item = self.selected_order.pop(index)
            self.selected_order.insert(index - 1, item)
            self._refresh_order_listbox(index - 1)
    
    def _move_down(self):
        """将选中的项下移"""    
        selection = self.order_listbox.curselection()
        if selection and selection[0] < len(self.selected_order) - 1:
            index = selection[0]
            item = self.selected_order.pop(index)
            self.selected_order.insert(index + 1, item)
            self._refresh_order_listbox(index + 1)
    
    def _refresh_order_listbox(self, select_index: int):
        """刷新顺序列表并选中指定项"""
        self.order_listbox.delete(0, tk.END)
        for item in self.selected_order:
            self.order_listbox.insert(tk.END, item)
        self.order_listbox.select_set(select_index)
    
    def _save_rename_rule(self)-> None:
        """保存重命名规则"""
        # 先更新复选框状态，确保与顺序列表一致
        for key in self.rule_options:
            self.rule_options[key].set(key in self.selected_order)
        
        # 保存规则
        self.rename_rule = {
            'options': {key: var.get() for key, var in self.rule_options.items()},
            'order': self.selected_order.copy()
        }
        
        print("保存的重命名规则:", self.rename_rule)
        self.rule_window.destroy()
    
    def preview_rename(self)-> None:
        """预览重命名效果"""
        # 检查是否已选择文件夹和创建规则
        if not hasattr(self, 'dir_path') or not self.dir_path:
            messagebox.showwarning("警告", "请先选择文件夹！")
            return
        
        if not self.rename_rule:
            messagebox.showwarning("警告", "请先创建命名规则！")
            return
        
        # 清空预览列表
        self._clear_preview_list()
        
        try:
            # 预览每个文件的新文件名
            for file in self.source_files:
                file_path = os.path.join(self.dir_path, file)
                new_name = self._generate_new_filename(file_path)
                if new_name:
                    self.preview_files.append(new_name)
                    self.preview_listbox.insert(tk.END, new_name)
            
            # 更新预览文件数量显示
            self.preview_label.config(text=f"预览文件名列表    文件数量: {len(self.preview_files)}")
            
        except Exception as e:
            messagebox.showerror("错误", f"生成预览失败: {str(e)}")
    
    def _generate_new_filename(self, file_path: str) -> str:
        """根据规则生成新文件名，仅从文件名中解析信息"""
        # 直接从文件名解析所有元数据
        metadata = self._parse_filename(file_path)
        
        # 获取文件扩展名和基础名称
        file_ext = os.path.splitext(os.path.basename(file_path))[1]
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # 根据规则生成新文件名各部分
        new_parts = self._build_filename_parts(metadata)
        
        # 使用连字符连接各部分
        new_name = '-'.join(new_parts) if new_parts else base_name
        
        # 添加文件扩展名
        new_name += file_ext
        
        # 清理非法字符
        new_name = self._sanitize_filename(new_name, base_name, file_ext)
        
        return new_name
    
    def _parse_filename(self, file_path: str) -> dict:
        """仅从原始文件名解析所有元数据，文件名格式为：来源@ID@标题@艺术家"""
        # 初始化默认元数据
        metadata = {
            'artist': '未知艺术家',
            'title': '未知标题',
            'source': '未知来源',
            'id': '未知ID'
        }
        
        filename = os.path.basename(file_path)
        base_name = os.path.splitext(filename)[0]
        
        # 检查文件名格式是否包含@分隔符（适用于"爱听"和"网易云"等格式）
        if '@' in base_name:
            parts = base_name.split('@')
            if len(parts) >= 1:
                # 提取来源
                metadata['source'] = parts[0]
            if len(parts) >= 2:
                # 提取ID
                metadata['id'] = parts[1]
            if len(parts) >= 3:
                # 提取标题，清理可能的额外信息
                title = parts[2]
                # 移除可能的副标题、电影信息等
                for keyword in ['-《', '（', '(', '【']:
                    if keyword in title:
                        title = title.split(keyword)[0]
                metadata['title'] = title.strip()
            if len(parts) >= 4:
                # 提取艺术家
                artist = parts[3]
                # 处理联合艺术家情况（如"艺术家1&艺术家2"）
                metadata['artist'] = artist.strip()
        
        return metadata
    
    def _build_filename_parts(self, metadata: dict) -> list:
        """构建文件名的各个部分"""
        parts = []
        
        # 检查规则格式
        if isinstance(self.rename_rule, dict):
            # 包含order字段
            if 'order' in self.rename_rule:
                # 按照用户定义的顺序添加各个部分
                for item in self.rename_rule['order']:
                    part = self._get_filename_part(item, metadata)
                    if part:
                        parts.append(part)  
        return parts
    
    def _get_filename_part(self, item: str, metadata: dict) -> str:
        """获取文件名的特定部分，仅使用从文件名解析的信息"""
        if item == '艺术家' and metadata.get('artist') and metadata.get('artist') != '未知艺术家':
            return metadata.get('artist')
        elif item == '标题' and metadata.get('title') and metadata.get('title') != '未知标题':
            return metadata.get('title')
        elif item == '来源' and metadata.get('source') and metadata.get('source') != '未知来源':
            return metadata.get('source')
        elif item == 'ID' and metadata.get('id') and metadata.get('id') != '未知ID':
            return metadata.get('id')
        return None
    
    def _sanitize_filename(self, filename: str, base_name: str, file_ext: str) -> str:
        """清理文件名中的非法字符"""
        # 用'&'替换非法文件名字符
        for char in self.ILLEGAL_CHARS:
            filename = filename.replace(char, '&')
        
        # 确保文件名不为空
        if not filename or filename == file_ext:
            filename = base_name + file_ext
            
        # 处理过长的文件名
        max_length = 200  # Windows文件名最大长度限制
        if len(filename) > max_length:
            name_without_ext = os.path.splitext(filename)[0]
            filename = name_without_ext[:max_length - len(file_ext)] + file_ext
            
        return filename
    
    def rename_files(self)-> None:
        """执行文件重命名操作"""
        # 检查预览文件是否准备好
        if not self.preview_files or len(self.preview_files) != len(self.source_files):
            messagebox.showwarning("预览错误", "请先生成预览文件名，且预览文件数量应与源文件数量一致！")
            return
        
        # 询问用户确认
        if not messagebox.askyesno("确认重命名", f"确定要重命名这 {len(self.source_files)} 个文件吗？此操作无法撤销。"):
            return
        
        # 执行重命名操作
        success_count = 0
        error_count = 0
        error_details = []
        
        try:
            for old_name, new_name in zip(self.source_files, self.preview_files):
                old_path = os.path.join(self.dir_path, old_name)
                new_path = os.path.join(self.dir_path, new_name)
                
                # 避免文件名冲突
                if os.path.exists(new_path) and old_name != new_name:
                    new_path = self._handle_file_conflict(new_path)
                
                try:
                    os.rename(old_path, new_path)
                    success_count += 1
                except Exception as e:
                    error_msg = f"{old_name} -> {new_name}（错误: {str(e)}）"
                    error_details.append(error_msg)
                    error_count += 1
            
            # 显示结果摘要
            result_message = f"成功重命名 {success_count} 个文件"
            if error_count > 0:
                result_message += f"，失败 {error_count} 个文件"
                # 简化错误信息显示，只显示前5个错误
                if len(error_details) > 5:
                    error_details = error_details[:5] + [f"... 还有 {len(error_details) - 5} 个错误"]
                error_text = "\n".join(error_details)
                messagebox.showwarning(
                    "重命名完成（部分失败）", 
                    f"{result_message}。\n\n失败详情：\n{error_text}"
                )
            else:
                messagebox.showinfo("重命名完成", f"{result_message}！")
                
            # 刷新文件列表
            self._load_audio_files()
            
        except Exception as e:
            messagebox.showerror("错误", f"重命名过程中发生错误: {str(e)}")
    
    def _handle_file_conflict(self, file_path: str) -> str:
        """处理文件名冲突"""
        base, ext = os.path.splitext(file_path)
        counter = 1
        
        while os.path.exists(file_path):
            file_path = f"{base}_{counter}{ext}"
            counter += 1
            
            # 避免无限循环
            if counter > 100:
                break
        
        return file_path


if __name__ == '__main__':
    # 创建应用实例，设置窗口大小为1200x600（更适合大多数显示器）
    app = AudioFilesRenamer(1200, 600)