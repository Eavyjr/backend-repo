import pytesseract
import cv2
from PIL import Image
import config

if hasattr(config, "TESSERACT_PATH"):
    pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Error loading image. Check if the file exists: {image_path}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.adaptiveThreshold(gray, 255, 
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 11, 2)
    pil_img = Image.fromarray(processed_img)
    text = pytesseract.image_to_string(pil_img, config="--psm 6")
    
    return text.strip()

# Example Usage:
text_result = extract_text_from_image("C:/Users/PHARM_CHIDIEBERE/Desktop/Project/backend/test_image.png")
print(text_result)
