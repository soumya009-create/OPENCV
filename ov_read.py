import cv2
import numpy as np
import mediapipe 
img=cv2.imread(r"opencv_tutorials/apu.png",1)

print(img)

small_img = cv2.resize(img, (700,500))  # width=400, height=300

cv2.imshow("Small Image", small_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



##place the pictures at the local file directory not one drive and plz did not change the name or the format of any file or images