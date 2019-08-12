#coding=utf8
'''
Created on 2019729

@author: zhangwc6
'''

import os
os.chdir('D:/work/gangjin/target')
import time
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

if __name__ == '__main__':
    fileList = os.listdir(".")
    fileList.remove('20.bmp')
    fileList.remove('21.bmp')
    fileList.remove('13.bmp')
    fileList.remove('14.bmp')
    fileList.remove('15.bmp')
    fileList.remove('1.bmp')
    fileList.remove('10.bmp')
    fileList.remove('11.bmp')
    fileList.remove('16.bmp')
    fileList.remove('17.bmp')
    fileList.remove('18.bmp')
    fileList.remove('2.bmp')
    fileList.remove('22.bmp')
    fileList.remove('24.bmp')
    fileList.remove('25.bmp')
    fileList.remove('26.bmp')
    fileList.remove('27.bmp')
    fileList.remove('3.bmp')
    fileList.remove('30.bmp')
    fileList.remove('31.bmp')
    fileList.remove('32.bmp')
    fileList.remove('33.bmp')
    fileList.remove('7.bmp')
    fileList.remove('8.bmp')
    fileList.remove('9.bmp')
    fileList.remove('demo.bmp')
    
    fileList.remove('23.bmp')
    fileList.remove('28.bmp')
#     fileList.remove('12.bmp')
#     fileList.remove('19.bmp')
    fileList.remove('4.bmp')
    fileList.remove('5.bmp')
    fileList.remove('6.bmp')
    
    for filename in fileList:#fileList
        if filename.endswith(".bmp"):
            print(filename)
            img = cv2.imread(filename)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            print(type(img))
            print(img.shape)
            print(np.min(img), np.max(img))
            
#             th2 = cv2.adaptiveThreshold(img, 1, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 0)
            ret, th2 = cv2.threshold(img, (np.min(img) + np.max(img))/9., 1, cv2.THRESH_BINARY)
            print(ret)
            print(np.min(th2), np.max(th2))
            print(np.unique(th2))
            plt.imshow(th2)
            plt.show()
            cv2.imwrite(filename[:-4] + ".png",th2,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])
#             cv2.imshow('th2', th2)
            time.sleep(1)
            
            
        