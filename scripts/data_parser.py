import json
import re

# Use the correct file path
text_file_path = "data/extracted_text.txt"
json_output_path = "data/extracted_data.json"

try:
    with open(text_file_path, "r", encoding="utf-8") as f:
        extracted_text = f.read()
except FileNotFoundError:
    print(f"❌ ERROR: '{text_file_path}' not found. Run `ocr_extraction.py` first.")
    exit(1)

# Extract patient details using regex
data = {}
data["patient_name"] = re.search(r"Patient Name\s*:\s*(.*)", extracted_text).group(1) if re.search(r"Patient Name\s*:\s*(.*)", extracted_text) else "Unknown"
data["dob"] = re.search(r"DOB\s*:\s*(\d{2}/\d{2}/\d{4})", extracted_text).group(1) if re.search(r"DOB\s*:\s*(\d{2}/\d{2}/\d{4})", extracted_text) else "Unknown"

# Save structured data as JSON
with open(json_output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ JSON Data Parsed Successfully! File saved in {json_output_path}")
