#coding=utf8
'''
Created on 2019年8月7日
查看图片属性
@author: zhangwc6
'''

import os
os.chdir('D:/work/gangjin')
# os.chdir('E:/test/images')
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

filename="5.jpg"
img = cv2.imread(filename)
img=Image.open(filename)
print(dir(img))
a=np.array(img)
print(a.shape, np.max(a), np.min(a))





