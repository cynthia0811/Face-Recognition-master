# import numpy
# import cv2

# face_cascade = cv2.CascadeClassifier(r'D:/Program Files(x86)/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
#
# img = cv2.imread("egg.jpg")
# print(type(img))
# cv2.imshow("Output1",img)
# cv2.waitKey(0)
#
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# # pathf = 'D:\\Program Files(x86)\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml'
# # pathf = r'D:/Program Files(x86)/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml'
# # face_cascade = cv2.CascadeClassifier(pathf)
# # another
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # face_cascade.load(r'D:/Program Files(x86)/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# # pathf = 'D:\\Program Files(x86)\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml'
# # face_cascade.load(pathf)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)


# # 这个函数里的image就是我们要检测的图片。在人脸检测程序的最后，我们会显示检测的结果图片来验证，这里做resize是为了避免图片过大，超出屏幕范围。
# def resize(image, width=1200):
#     r = width *1.0/ image.shape[1]
#     dim = (width,int(image.shape[0] * r))
#     resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
#     return resized
#
#
# import cv2
# filename='hezhao2.jpg'
#
# face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# img=cv2.imread(filename)
# img = resize(img, width=1200)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces=face_cascade.detectMultiScale(gray,1.3,5)
# for (x,y,h,w) in faces:
#     img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# cv2.namedWindow('faces Detected!')
# cv2.imshow('faces Detected!',img)
# cv2.imwrite('faces.jpg',img)
# cv2.waitKey(0)

import cv2
img = cv2.imread(r'D:/my_laboratory/face_detection20180516/faceRecognition-master/hezhao2.jpg')
cv2.imshow("Output1",img)
cv2.waitKey(0)
