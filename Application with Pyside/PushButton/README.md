# PySide6 Button Signals Demo — شرح + Documentation  
(English version included below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع يوضّح كيفية التعامل مع **إشارات الأزرار (Button Signals)** في PySide6.  
يوجد زر واحد فقط، لكنه مرتبط بثلاث إشارات مهمة:

- `pressed` → عند الضغط على الزر  
- `released` → عند رفع اليد  
- `clicked` → عند الضغط ثم الإفلات  

وكل إشارة مرتبطة بدالة تطبع نصًا مختلفًا في الطرفية.

---

## 📁 ملفات المشروع

### **1️⃣ main.py**
يشغّل التطبيق:
- ينشئ `QApplication`
- ينشئ نافذة من كلاس `window`
- يعرض الواجهة
- يبدأ الحلقة الرئيسية

### **2️⃣ Widget.py**
واجهة بسيطة تحتوي على:
- زر واحد
- ثلاث إشارات:
  - `clicked`
  - `pressed`
  - `released`
- ثلاث دوال مرتبطة:
  - `click()` → تطبع "Clicked"
  - `press()` → تطبع "Pressed"
  - `release()` → تطبع "Released"

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project demonstrates **button signals** in PySide6.  
It uses one button connected to three core signals:

- `pressed`  
- `released`  
- `clicked`  

Each signal triggers a different function that prints a specific message.

---

## 📁 Project Structure

### **1️⃣ main.py**
Entry point:
- Creates QApplication  
- Instantiates the window  
- Shows the interface  
- Starts the event loop  

### **2️⃣ Widget.py**
Defines the UI:
- A single QPushButton
- Three connected signals:
  - `clicked` → prints “Clicked”
  - `pressed` → prints “Pressed”
  - `released` → prints “Released”
- Simple vertical layout
