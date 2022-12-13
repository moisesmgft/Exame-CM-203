import cv2
import numpy as np

def ellipse_detection(img):
  img = cv2.medianBlur(img,5)      

  circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,.5, 30,
                              param1=130,param2=70,minRadius=3)
  center = []

  if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
      center.append((i[0],i[1]))

  return center