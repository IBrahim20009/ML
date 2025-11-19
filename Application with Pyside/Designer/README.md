# PySide6 User Form — مشروع واجهة إدخال بيانات  
(English version below)

## 🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن واجهة رسومية بسيطة باستخدام **PySide6** و **Qt Designer**.  
المستخدم يقوم بإدخال:
- الاسم الكامل  
- الوظيفة أو الدور  

وبالضغط على زر **Submit** يتم طباعة البيانات بصيغة:

```
Ahmad is a Developer
```

---

## 📁 مكونات المشروع

### 1️⃣ main.py
ملف التشغيل الأساسي:
- ينشئ التطبيق
- يحمّل الواجهة من widget.py
- يعرض النافذة
- يبدأ الحلقة الرئيسية

### 2️⃣ widget.py
يتعامل مع الواجهة التي تم إنشاؤها في Qt Designer:
- تحميل `untitled.ui`
- ربط زر Submit بدالة
- قراءة الحقول lineEditForFullname و lineEditForRole
- طباعة البيانات

### 3️⃣ untitled.ui
واجهة Qt Designer:
- QLineEdit لاسم المستخدم
- QLineEdit للدور
- زر Submit

### 4️⃣ resource.qrc
ملف الموارد (صور - أيقونات - ملفات إضافية).

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Version

## Overview
This is a simple **PySide6 GUI app** built using **Qt Designer**.  
The user enters:
- Full name  
- Role / Job title  

Pressing **Submit** prints:

```
Ahmad is a Developer
```

---

## Project Structure

### 1️⃣ main.py
Application entry point:
- Creates QApplication  
- Loads UserInterface  
- Shows the window  
- Starts the event loop  

### 2️⃣ widget.py
Controls UI loaded from Qt Designer:
- Loads `untitled.ui`
- Connects Submit button
- Reads text fields
- Prints the formatted output

### 3️⃣ untitled.ui
Designer layout:
- Two QLineEdit fields
- One QPushButton named Submit

### 4️⃣ resource.qrc
Resource file containing icons/images if needed.
