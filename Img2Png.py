#coding=utf8
'''
Created on 2019729
图片格式转换工具类
@author: zhangwc6
'''

from PIL import Image
import os
os.chdir('D:/work/gangjin/target')

fileList = os.listdir(".")
for filename in fileList:
    if filename.endswith(".png"):
        im = Image.open(filename)
        im.save(filename[:-4] + ".png")
