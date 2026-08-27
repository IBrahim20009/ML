# PySide6 Text Editor — شرح + Documentation  
(English version below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن محرر نصوص بسيط باستخدام **PySide6**.  
يوفّر مجموعة من الوظائف الأساسية مثل النسخ، القص، التراجع، الإعادة، ومسح النص — مباشرة من خلال دوال `QTextEdit` الجاهزة.

---

## 📁 ملفات المشروع

### **1️⃣ main.py**
الملف المسؤول عن تشغيل التطبيق:
- ينشئ `QApplication`
- يستدعي الواجهة `Widget`
- يعرض النافذة
- يبدأ الحلقة الرئيسية

---

### **2️⃣ widget.py**
واجهة التحرير وتتضمن:
- `QTextEdit` لكتابة النص
- مجموعة أزرار:
  - Copy
  - Cut
  - Undo
  - Redo
  - Clear  
- كل زر متصل مباشرة بدالة جاهزة داخل QTextEdit
- تخطيط أفقي للأزرار وتخطيط عمودي لدمج الواجهة كاملة

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project is a simple **text editor GUI** built with PySide6.  
It provides basic editing functions using built-in QTextEdit slots.

---

## 📁 Project Structure

### **1️⃣ main.py**
Entry point:
- Creates QApplication  
- Instantiates the Widget  
- Shows the GUI  
- Runs the event loop  

---

### **2️⃣ widget.py**
Contains:
- A QTextEdit for text input  
- Buttons for:
  - Copy  
  - Cut  
  - Undo  
  - Redo  
  - Clear  
- Buttons are connected directly to QTextEdit slots  
- Clean layout using QHBoxLayout + QVBoxLayout  

---


