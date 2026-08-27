# PySide6 ComboBox Controller — شرح + Documentation  
(English explanation below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن واجهة بسيطة باستخدام **PySide6** للتعامل مع QComboBox.  
المستخدم يستطيع:
- رؤية القيمة الحالية
- تغيير القيمة للعنصر الثاني
- عرض كل العناصر داخل الـ combo

---

## 📁 ملفات المشروع

### **1️⃣ main.py**
يشغّل التطبيق:
- ينشئ QApplication  
- ينشئ نافذة من widget  
- يعرض الواجهة  
- يبدأ الحلقة الرئيسية  

### **2️⃣ widget.py**
يحتوي على الواجهة والعناصر:
- QComboBox بخيارين: `hyper`, `CKD`
- زر *Current value* لعرض القيمة الحالية
- زر *set value* لتغيير الاختيار إلى CKD
- زر *get value* لعرض جميع العناصر
- دوال المعالجة:
  - `Currentvalue()`  
  - `setcurrent()`  
  - `getvalues()`  

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project is a simple **PySide6 GUI** demonstrating basic interaction with a QComboBox.  
The user can:
- Display the current selected value  
- Set the value programmatically  
- List all available combo items  

---

## 📁 Project Structure

### **1️⃣ main.py**
Entry point:
- Creates QApplication  
- Instantiates the widget  
- Shows the GUI  
- Runs the event loop  

### **2️⃣ widget.py**
Implements the UI:
- QComboBox with items: `hyper`, `CKD`
- Buttons:
  - *Current value* → prints selected text + index  
  - *set value* → sets index to 1  
  - *get value* → prints all items  
- Layout handled with QVBoxLayout  

---


