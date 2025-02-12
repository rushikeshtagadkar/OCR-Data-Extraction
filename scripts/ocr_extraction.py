import cv2
import pytesseract
import os

# Folder containing images
image_folder = "data"
text_output_path = "data/extracted_text.txt"

# Get all image files
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".jpg")])

if not image_files:
    print("❌ ERROR: No images found. Did the PDF convert properly?")
    exit(1)

extracted_text = ""

for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)
    
    # Load image and preprocess
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(gray)
    extracted_text += text + "\n"

    print(f"✅ Extracted text from {img_file}:\n{text[:500]}")  # Print first 500 characters

# Save extracted text to file
with open(text_output_path, "w", encoding="utf-8") as f:
    f.write(extracted_text)

print(f"✅ OCR Extraction Completed! Text saved in {text_output_path}")
