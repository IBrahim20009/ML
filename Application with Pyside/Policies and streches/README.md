# PySide6 Simple Layout Example — شرح + Documentation  
(English version below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع يوضّح كيفية إنشاء واجهة بسيطة باستخدام **PySide6** تحتوي على:
- Label لعرض نص ثابت
- QLineEdit لإدخال نص
- ضبط حجم العناصر باستخدام QSizePolicy
- تخطيط أفقي مع نسب تمدد مختلفة

الهدف هو تعلم كيفية التحكم في حجم العناصر داخل التخطيط باستخدام Python + PySide6.

---

## 📁 ملفات المشروع

### **1️⃣ widget.py**
يحتوي على الواجهة:
- `QLabel("Some text :")`
- `QLineEdit()` لإدخال النص
- إعداد size policy:
  - Expanding أفقياً
  - Fixed عامودياً
- تخطيط أفقي مع نسب تمدد (1 للـ label و 10 للـ input)

### **2️⃣ main.py**
يشغّل التطبيق:
- ينشئ `QApplication`
- ينشئ نافذة من كلاس widget
- يعرض الواجهة
- يبدأ الحلقة الرئيسية للتطبيق

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project demonstrates how to build a simple PySide6 interface with:
- A static text label  
- A QLineEdit input  
- Size control using QSizePolicy  
- A horizontal layout with stretch factors  

It is a clean example of layout and resizing behavior.

---

## 📁 Project Structure

### **1️⃣ widget.py**
Defines the UI:
- A QLabel displaying “Some text :”
- A QLineEdit for user input
- Size policies:
  - Expanding horizontally  
  - Fixed vertically  
- Horizontal layout with stretch factors (1 : 10)

### **2️⃣ main.py**
Entry point:
- Creates QApplication  
- Instantiates the widget  
- Shows the GUI  
- Runs the event loop  

---


