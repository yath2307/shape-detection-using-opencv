import serial
import time
def vid():
    import cv2

    cam = cv2.VideoCapture(1)
    
    img_counter = 0
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 32:
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            break
    cam.release()
    
    cv2.destroyAllWindows()
def vid2():
    import cv2
    fram=[]

    cam = cv2.VideoCapture(1)
    
    cv2.namedWindow("test")
    
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        fram.append(frame)
        if(img_counter > 100):
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, fram[50])
            print("{} written!".format(img_name))
            break
        img_counter += 1
    cam.release()
    cv2.destroyAllWindows()


def fun():
    import cv2
    import numpy as np
    vid()
    img=cv2.imread("opencv_frame_0.png",1)
    imw=img
    cv2.imshow("cndj",img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    shape = "unidentified"
    im = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    ima = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    count = 25
    while shape=="unidentified":
        count+=25
        ret1,th1 = cv2.threshold(ima,count,255,cv2.THRESH_BINARY_INV)
        cv2.imshow("bvjb",th1)
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        shape = "unidentified"
        im2, c, hierarchy = cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(c)>0:
            max=cv2.contourArea(c[0])
            index=c[0]
            for i in c:
                area = cv2.contourArea(i)
                if area>max:
                    max=area
                    index=i
            peri = cv2.arcLength(index, True)
            approx = cv2.approxPolyDP(index, 0.04 * peri, True)
            cv2.drawContours(imw, index, -1, (0, 255, 0), 2)
            cv2.imshow("hhgju", imw)
            cv2.waitKey(500)
            cv2.destroyAllWindows()
            if len(approx) == 3 and (peri*peri/cv2.contourArea(index))>=18 and (peri*peri/cv2.contourArea(index))<=23:
                    shape = "triangle"
            elif len(approx) == 4 and (peri*peri/cv2.contourArea(index))>=14 and (peri*peri/cv2.contourArea(index))<=18:
                    (x, y, w, h) = cv2.boundingRect(approx)
                    ar = w / float(h)
                    shape = "square" if ar >= 0.90 and ar <= 1.10 else "rectangle"
            elif len(approx) > 4 and (peri*peri/cv2.contourArea(index))>=11 and (peri*peri/cv2.contourArea(index))<=14:
                    shape = "circle"
        else:
            continue
    print(len(approx))
    return shape
def fun2():
    import cv2
    import numpy as np
    vid2()
    img=cv2.imread("opencv_frame_101.png",1)
    img = img[:400,:]
    imw=img
    cv2.imshow("cndj",img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    shape = "unidentified"
    im = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    ima = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    count = 25
    while shape=="unidentified":
        count+=25
        ret1,th1 = cv2.threshold(ima,count,255,cv2.THRESH_BINARY_INV)
        cv2.imshow("bvjb",th1)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
        shape = "unidentified"
        im2, c, hierarchy = cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(c)>0:
            max=cv2.contourArea(c[0])
            index=c[0]
            for i in c:
                area = cv2.contourArea(i)
                if area>max:
                    max=area
                    index=i
            peri = cv2.arcLength(index, True)
            approx = cv2.approxPolyDP(index, 0.04 * peri, True)
            cv2.drawContours(imw, index, -1, (0, 255, 0), 2)
            cv2.imshow("hhgju", imw)
            cv2.waitKey(500)
            cv2.destroyAllWindows()
            if len(approx) == 3 and (peri*peri/cv2.contourArea(index))>=18 and (peri*peri/cv2.contourArea(index))<=23:
                    shape = "triangle"
            elif len(approx) == 4 and (peri*peri/cv2.contourArea(index))>=14 and (peri*peri/cv2.contourArea(index))<=18:
                    (x, y, w, h) = cv2.boundingRect(approx)
                    ar = w / float(h)
                    shape = "square" if ar >= 0.90 and ar <= 1.10 else "rectangle"
            elif len(approx) > 4 and (peri*peri/cv2.contourArea(index))>=11 and (peri*peri/cv2.contourArea(index))<=14:
                    shape = "circle"
        else:
            continue
    print(len(approx))
    return shape

#arduino = serial.Serial("COM5",115200)
#time.sleep(2)
    
a=fun()
t=0
while t==0:
    b=fun2()
    print(b)
    if b==a:
        t-=1
        c="f"
        #arduino.write(b'f')
    else:
        c="l"
        arduino.write(b'l')
        #while True:
            #cm=arduino.read()
            #if cm=='y':
                #break
print(a,b,c)
