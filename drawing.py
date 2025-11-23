import cv2

img=cv2.imread(r"opencv_tutorials/apu.png",-1)

print(img)

small_img = cv2.resize(img, (700,500))  # width=400, height=300
img=cv2.line(small_img,(0,0),(255,255),(255,16,255),4)  # first part is the image part,starting and 
#ending co-ordinates,colors in the bgr format,thickness
img=cv2.arrowedLine(small_img,(345,0),(0,345),(255,16,255),4)
img=cv2.rectangle(small_img,(344,0),(0,344),(0,255,0),1)
img=cv2.circle(small_img,(255,255),45,(0,244,244),1)
cv2.imshow("Small Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()