# -*- coding: utf-8 -*-

from PIL import Image
from math import pi, log, exp
import numpy as np
import sys

def main(filename, r):
    # должна обрабатывать чб файл <filename> в формате PNG, уравнивать гистограмму
    # и записывать результат в <filename>.equalized.png
    img = Image.open(filename)
    img.load()
 
   # код сюда ....

    a = np.array(img.getdata(),dtype=np.uint8)
    a=a[:,0]
    a = a.reshape(img.size[::-1])
    b = np.zeros(img.size[::-1], dtype=np.uint8)
    
    m, n = a.shape
    
    #у img.histogram() почему-то длина 512 вместо 256, пришлось собрать вручную
    h = [0.0] * 256
    for i in range(m):
        for j in range(n):
            h[a[i, j]]+=1
    hist = np.array(h)/(m*n)
    
    cdf = np.cumsum(hist)
    sk = np.uint8(255 * cdf)
    s1, s2 = a.shape
    
    for i in range(0, s1):
        for j in range(0, s2):
            b[i, j] = sk[a[i, j]]

    newimg = Image.fromarray(b);
    newimg.show()
    newimg.save(filename+'.equalized.png')



if __name__=='__main__':
    # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png
    if len(sys.argv) > 1:
        main(sys.argv[1], r=3)
    else:
        print("Must give filename.\n")




