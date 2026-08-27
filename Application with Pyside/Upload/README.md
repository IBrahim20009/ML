# PySide6 File Upload Dialog — شرح + Documentation  
(English version below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن واجهة بسيطة مبنية باستخدام **PySide6**، تتيح للمستخدم اختيار أي ملف من جهازه عبر نافذة `QFileDialog`.  
بعد اختيار الملف، يتم عرض مساره على الشاشة.

---

## 📁 مكوّنات المشروع

### **1️⃣ زر Upload File**
- يفتح نافذة اختيار الملفات  
- يستخدم `QFileDialog.getOpenFileName()`  
- تم تنسيقه بلون وخلفية خاصة

### **2️⃣ QLabel**
- يعرض النص الافتراضي: *No file selected*  
- يتغيّر تلقائيًا عند اختيار ملف

### **3️⃣ QVBoxLayout**
- لتنظيم العناصر بشكل عمودي:
  - الزر
  - ثم الـ label

### **4️⃣ الدالة upload_file()**
- تفتح نافذة اختيار الملفات  
- تتحقق من اختيار المستخدم  
- تحدّث النص في الـ label على هذا الأساس

---

## ▶️ طريقة التشغيل

```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project is a simple **PySide6 GUI** that lets the user select a file using a standard `QFileDialog`.  
After the user picks a file, its full path is displayed on the screen.

---

## 📁 Project Structure

### **1️⃣ Upload Button**
- Opens a file selection dialog  
- Uses `QFileDialog.getOpenFileName()`  
- Styled using CSS

### **2️⃣ QLabel**
- Shows *No file selected* initially  
- Displays selected file path afterward

### **3️⃣ QVBoxLayout**
- Arranges the upload button above the label

### **4️⃣ upload_file() function**
- Opens the dialog  
- Checks whether a file was selected  
- Updates the label accordingly

---


