import cv2

def draw_line(path):
    img = cv2.line(image,start_p, end_p, color, thick)
    return img

def display_image():
    # Use raw string (r"") to handle Windows file paths correctly
    path = r"C:\Users\a\Pictures\WhatsApp Image 2024-12-28 at 23.38.12_e638c0b6.jpg"
    
    # Load the image
    img = cv2.imread(path)
    
    # Check if image was loaded successfully
    if img is None:
        print("Error: Could not load image. Please check the file path.")
        return
    
    # Define line parameters
    start_point = (50, 50)    # Starting point (x, y)
    end_point = (200, 200)    # Ending point (x, y)
    color = (0, 255, 0)       # Color in BGR format (Green)
    thickness = 3             # Line thickness
    
    # Draw line on the image
    img_with_line = cv2.line(img, start_point, end_point, color, thickness)
    
    # Display the image
    cv2.imshow("Image with Line", img_with_line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function
display_image()