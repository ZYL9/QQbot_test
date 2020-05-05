from os import listdir
import random


def listd():
    dataset_list = listdir("PixivImage")
    return dataset_list


def randompic():
    dataset_list = listd()
    length = len(dataset_list)
    output = dataset_list[random.randint(0, length)]
    return output
