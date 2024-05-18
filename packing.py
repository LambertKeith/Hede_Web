import os
import shutil
import zipfile



class PackerParam:
    def __init__(self) -> None:
        self.source_settings_path = 'web_demo/web_demo/settings.py'
        self.target_settings_path = 'zip_files/web_demo/settings.py'
        self.zip_folder = 'zip_files'
        self.requirements_path = 'requirements.txt'
        self.project_path = 'web_demo'
        

class Packer:
    def __init__(self) -> None:
        # 获取路径
        self.param = PackerParam()

        # 初始化操作目录
        self.make_zip_dir()

        # 复制项目
        self.copy_folder_contents()

        # 复制依赖
        self.copy_file(self.param.requirements_path, self.param.zip_folder)

        # 覆盖配置
        self.alter_settings()

        # 打包
        self.zip_folder()


    def alter_settings(self):
        """修改settings.py
        """        
        # 读取原始文件
        with open(self.param.source_settings_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # 替换数据库信息
        new_content = original_content.replace(
            "'NAME': 'web_test'",
            "'NAME': 'web_test'"
        ).replace(
            "'USER': 'root'",
            "'USER': 'app01'"
        ).replace(
            "'PASSWORD': '111111'",
            "'PASSWORD': '111111'"
        )

        # 写入更新后的内容到新文件
        with open(self.param.target_settings_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print("替换完成！")


    def make_zip_dir(self):
        """目录初始化
        """        
        path = self.param.zip_folder
        if not os.path.exists(path):  # 如果路径不存在
            os.makedirs(path)  # 创建文件夹
        else:
            # 如果路径存在，则清空文件夹
            shutil.rmtree(path)
            os.makedirs(path)


    def copy_folder_contents(self):
        """项目复制
        """        
        source_folder = self.param.project_path
        destination_folder = self.param.zip_folder

        # 获取源文件夹下的所有内容
        contents = os.listdir(source_folder)
        
        # 遍历内容，并复制到目标文件夹中
        for item in contents:
            # 构建源路径和目标路径
            source_path = os.path.join(source_folder, item)
            destination_path = os.path.join(destination_folder, item)
            
            # 如果是文件，则直接复制
            if os.path.isfile(source_path):
                shutil.copy(source_path, destination_path)
            # 如果是文件夹，则递归复制其内容
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)


    def copy_file(self, source_file, destination_folder):
        # 使用shutil.copy()函数将文件复制到目标文件夹
        shutil.copy(source_file, destination_folder)


    def zip_folder(self):
        """打包
        """        
        folder_path = self.param.zip_folder
        zip_path = 'web.zip'
        # 创建一个新的 zip 文件
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 遍历文件夹下的所有内容
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # 构建文件的完整路径
                    file_path = os.path.join(root, file)
                    # 添加文件到 zip 压缩包中
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))