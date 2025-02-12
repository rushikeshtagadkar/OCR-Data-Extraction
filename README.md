# OCR-Based Data Extraction Project

## 📌 Overview
This project automates text extraction from scanned patient assessment forms using Optical Character Recognition (**OCR**). The extracted text is structured into **JSON format** and stored in a **PostgreSQL database**.

## 🚀 Features
- Extracts text from **PDF/JPEG** using **Tesseract OCR**
- Converts unstructured text into **structured JSON**
- Stores extracted data in a **PostgreSQL database**
- Provides a clean **SQL schema**
- Open-source and easy to set up

---
📂 Project Structure
```
📂 OCR-Data-Extraction
 ┣ 📂 data
 ┃ ┣ oaksol_Intern_OCR_Assignment.pdf
 ┃ ┣ extracted_text.txt
 ┃ ┣ extracted_data.json
 ┣ 📂 scripts
 ┃ ┣ ocr_extraction.py
 ┃ ┣ data_parser.py
 ┃ ┣ database_insert.py
 ┣ sql_schema.sql
 ┣ README.md
 ┣ requirements.txt
 ```
---

### 🛠 Setup & Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/rushikeshtagadkar/OCR-Data-Extraction.git
cd OCR-Data-Extraction
```

### 2️⃣ Create & Activate Virtual Environment
```
python -m venv venv
```
Windows:

```
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Ensure Tesseract OCR is Installed

Windows: [Download Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)


### 5️⃣ Ensure Poppler is Installed

Windows: [Download Poppler](https://github.com/oschwartz10612/poppler-windows/releases)

---
### 🔄 Usage Instructions

### 1️⃣ Run OCR Extraction
```
python scripts/ocr_extraction.py
```
Output: Extracted text saved in data/extracted_text.txt

### 2️⃣ Convert Extracted Text to JSON
```
python scripts/data_parser.py
```
Output: JSON data saved in data/extracted_data.json

### 3️⃣ Store JSON Data in PostgreSQL
```
python scripts/database_insert.py
```
Output: Data inserted into the PostgreSQL database.
