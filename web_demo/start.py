import os

def start_django_server():
    # 切换到 Django 项目目录
    #os.chdir('/path/to/your/django/project')

    # 启动 Django 服务
    os.system('python3 manage.py runserver 0.0.0.0:8082')

if __name__ == "__main__":
    start_django_server()
