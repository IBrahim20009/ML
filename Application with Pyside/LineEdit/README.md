# PySide6 Live Text Input — شرح + Documentation  
(English version included below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن تطبيق بسيط باستخدام **PySide6** يقوم بعرض النص الذي يكتبه المستخدم داخل `QLineEdit`.  
كما يمكن عرض النص عند الضغط على زر **Grab data**.

---

## 📁 ملفات المشروع

### **1️⃣ main.py**
الملف المسؤول عن تشغيل البرنامج:
- ينشئ تطبيق PySide6
- ينشئ الواجهة من كلاس widget
- يعرض النافذة
- يبدأ الحلقة الرئيسية

### **2️⃣ widget.py**
الملف الذي يحتوي على الواجهة:
- Label لطلب الاسم
- QLineEdit لإدخال النص
- زر Grab data
- Label لعرض النص
- دالة `textchanges()` لعرض النص فورًا أثناء الكتابة
- دالة `GrabData()` لعرض النص عند الضغط على الزر

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This is a simple **PySide6 GUI application** that displays the text typed by the user.  
The display updates either:

- **Live while typing** (real-time), or  
- **When clicking the “Grab data” button**

---

## 📁 Project Structure

### **1️⃣ main.py**
The entry point:
- Creates the QApplication  
- Instantiates the widget  
- Shows the GUI  
- Runs the event loop  

### **2️⃣ widget.py**
Implements the GUI:
- A label prompting for a full name  
- A QLineEdit text field  
- A “Grab data” button  
- Output label  
- `textchanges()` for live updates  
- `GrabData()` to update on button press  
