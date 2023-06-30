import cv2
import pytesseract

imname = "sample1.png"

image = cv2.imread(f"images/{imname}")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(image)
print(text)