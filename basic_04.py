import cv2
import os

def draw_line(path):
    image = cv2.imread(path)

    if image is None:
        print(f"Error: Image not found at {path}")
        return None

    start = (0, 0)
    end = (500, 500)
    color = (0, 255, 0)
    thick = 10

    img = cv2.line(image, start, end, color, thick)
    return img

def display_image():
    path = r"opencv_tutorials/soumya.png"
    img = draw_line(path)

    if img is not None:
        cv2.imshow("apu.png", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

display_image()  # Only call it once
