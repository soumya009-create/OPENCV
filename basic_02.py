import cv2
import os

img_path = "opencv_tutorials/WhatsApp Image 2025-03-25 at 11.32.23_9d23cce1.jpg"

img = cv2.imread(img_path)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()