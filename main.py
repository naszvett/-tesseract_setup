import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

file_path = "free_stock_photoes_pexels_dot_com.jpeg"
img = cv.imread(file_path)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

print(pytesseract.image_to_string(img))