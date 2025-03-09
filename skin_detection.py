import cv2
import numpy as np

def detect_skin(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error: Unable to read image")
    
    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define skin color range in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Threshold the image to get skin areas
    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Apply morphological operations to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_OPEN, kernel)
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_CLOSE, kernel)
    
    # Convert mask to binary image (skin areas are white, others are black)
    skin_image = cv2.bitwise_and(image, image, mask=skin_mask)
    
    # Convert to grayscale and threshold for a binary output
    gray_skin = cv2.cvtColor(skin_image, cv2.COLOR_BGR2GRAY)
    _, binary_skin = cv2.threshold(gray_skin, 1, 255, cv2.THRESH_BINARY)
    
    # Save and return the processed image
    output_path = "skin_detected.png"
    cv2.imwrite(output_path, binary_skin)
    return output_path

if __name__ == "__main__":
    image_path = "face.jpg"  # Replace with actual image path
    output = detect_skin(image_path)
    print(f"Skin detection saved at: {output}")

