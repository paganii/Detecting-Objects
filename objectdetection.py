import cv2
import numpy as np

image = cv2.imread("flowerr.png", 1) #read color
print(image.shape)
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(grayimg.shape) #shape tells the height weight and px of pic
blurredimg = cv2.blur(grayimg, (3,3))
print(blurredimg)
detectingcircles = cv2.HoughCircles(blurredimg, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)
if detectingcircles is not None:
    print(detectingcircles)
    detectingcircles = np.uint16(np.around(detectingcircles))
    for i in detectingcircles:
        x, y, r = i[0], i[1], i[2]
        cv2.circle(image, (x,y), r, (0,0,255), 2) #boundar
        cv2.circle(image, (x,y), 1, (0,255,255), 3)
    cv2.imshow("Detected Circles", image)
    cv2.waitKey()


