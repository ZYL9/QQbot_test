#随机选择

import base64
from os import listdir
import random

# import os,sys
# project_path = os.path.dirname(os.path.abspath(__file__)) # 获取当前文件路径的上一级目录


def listd():
    dataset_list = listdir("PixivImage")
    return dataset_list


def randompic():
    dataset_list = listd()
    length = len(dataset_list)
    output = dataset_list[random.randint(0, length)]
    return output


def picbase():
    with open(dir, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    return s


num = randompic()
dir = './PixivImage/' + num