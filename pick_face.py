#-*-coding:utf8-*-
# __author__ = '尹籽'

import os
import cv2
import time
from read_img import readAllImg

#从源路径中读取所有图片放入一个list，然后逐一进行检查，把其中的脸扣下来，存储到目标路径中
def readPicSaveFace(sourcePath,objectPath,*suffix):
    try:
        #读取照片,注意第一个元素是文件名
        resultArray=readAllImg(sourcePath,*suffix)
        # print(resultArray)
        #对list中图片逐一进行检查,找出其中的人脸然后写到目标文件夹下
        count = 1
        # face_cascade = cv2.CascadeClassifier('E:\openCV\opencv\sources\data\haarcascades\
        # D:\Program Files (x86)\opencv\sources\data\haarcascades
        # face_cascade = cv2.CascadeClassifier(r'D:/Program Files(x86)/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
        # pathf = 'D:\\Program Files(x86)\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml'
        # pathf = r'D:/Program Files(x86)/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml'
        # face_cascade = cv2.CascadeClassifier(pathf)
        # another
        # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # face_cascade = cv2.CascadeClassifier(r'D:/my_laboratory/face_detection20180516/source - cynthia/haarcascade_frontalface_alt.xml')
        # face_cascade.load(r'D:/Program Files(x86)/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        # print(len(resultArray))
        for i in resultArray:
            print(type(i))
            if type(i) != str:
                gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    listStr = [str(int(time.time())), str(count)]  #以时间戳和读取的排序作为文件名称
                    fileName = ''.join(listStr)
                    # f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
                    f = cv2.resize(gray[y:(y + h), x:(x + w)], (250, 250))
                    # # print(type(f))
                    # cv2.imshow("Output1",f)
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
                    # cv2.imwrite(objectPath+os.sep+'%s.jpg' % fileName, f)
                    cv2.imwrite(objectPath+'%s.jpg' % fileName, f)
                    count += 1

    except IOError:
        print ("Error")

    else:
        print ('Already read '+str(count-1)+' Faces to Destination '+objectPath)

if __name__ == '__main__':
     # readPicSaveFace('D:\myProject\pictures\source-jerry','D:\myProject\pictures\picTest','.jpg','.JPG','png','PNG')
     readPicSaveFace(r'D:/my_laboratory/face_detection20180516/picture_save/1', r'D:/my_laboratory/face_detection20180516/picture_save/2','.jpg','.JPG','.png','.PNG')
