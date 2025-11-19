# PySide6 MessageBox Demo — شرح + Documentation  
(English version below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع يوضح كيفية استخدام **QMessageBox** في PySide6 بالإضافة إلى كيفية التعامل مع الأزرار والأحداث (signals & slots).

يحتوي التطبيق على 5 أزرار، كل زر يعرض أو يطبع نوعًا مختلفًا من الرسائل:
- رسالة Critical منبثقة
- رسالة Information
- رسالة Question
- رسالة Warning
- طباعة Normal Critical

---

## 📁 مكوّنات المشروع

### **1️⃣ main.py**
ملف التشغيل:
- ينشئ التطبيق
- يستدعي الواجهة Widget
- يعرض النافذة
- يبدأ الحلقة الرئيسية

### **2️⃣ widget.py**
يحتوي على:
- خمسة أزرار
- كل زر مرتبط بدالة خاصة
- دالة `hardfunc()` تعرض QMessageBox من نوع Critical
- باقي الدوال تطبع نصوص في الطرفية

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project demonstrates the usage of **QMessageBox** in PySide6 along with button actions.

The application contains 5 buttons:
- A Critical popup message
- A simple Critical print message
- Question print message
- Information print message
- Warning print message

---

## 📁 Project Structure

### **1️⃣ main.py**
Entry point:
- Creates QApplication  
- Instantiates the Widget  
- Shows the GUI  
- Runs the event loop  

### **2️⃣ widget.py**
Contains:
- Five buttons  
- Each button connected to a specific function  
- `hardfunc()` shows a Critical QMessageBox  
- Other functions print simple output  

---


