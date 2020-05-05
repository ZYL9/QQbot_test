import base64
from tupian import randompic

# import os,sys
# project_path = os.path.dirname(os.path.abspath(__file__)) # 获取当前文件路径的上一级目录
num = randompic()
dir = './PixivImage/' + num


def picbase():
    with open(dir, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    return s
