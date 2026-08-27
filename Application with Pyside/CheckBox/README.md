# PySide6 OS Selector — شرح + Documentation

## 🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن واجهة رسومية بسيطة باستخدام **PySide6** تسمح للمستخدم باختيار نظام التشغيل من خيارين:
- Windows  
- Linux  

عند اختيار أحدهما، يتم طباعة رسالة مختلفة في وحدة الإخراج.

## 📁 مكونات المشروع

### 1️⃣ main.py
الملف المسؤول عن تشغيل التطبيق:
- ينشئ QApplication
- ينشئ نافذة من widget
- يعرض الواجهة
- يشغل الحلقة الرئيسية

### 2️⃣ Widget.py
يحتوي على المنطق الأساسي للواجهة:
- زرين من نوع RadioButton
- مجموعة اختيار حصرية (ButtonGroup)
- دوال مرتبطة بالنقر:
  - Windows → تطبع “hj”
  - Linux → تطبع “hi from linux”
  
---

## 🇺🇸 English Documentation

This project is a simple **PySide6 GUI** that allows the user to select between two operating systems:
- Windows  
- Linux  

Each selection triggers a different print message in the terminal.

## 📁 Project Structure

### 1️⃣ main.py
Responsible for running:
- Creates `QApplication`
- Initializes a `widget` window
- Shows the GUI
- Starts the main event loop

### 2️⃣ Widget.py
Implements the UI logic:
- Two `QRadioButton`s
- Exclusive `QButtonGroup`
- Connected slots:
  - Windows → prints “hj”
  - Linux → prints “hi from linux”
