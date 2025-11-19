# PySide6 Image Viewer — شرح + Documentation  
(English version below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن واجهة بسيطة باستخدام **PySide6** لعرض صورة داخل نافذة.  
يتم تحميل الصورة باستخدام `QPixmap` ثم عرضها داخل `QLabel`، ويتم ترتيبها في منتصف الشاشة باستخدام تخطيط عمودي `QVBoxLayout`.

---

## 📁 ملفات المشروع

### **1️⃣ main.py**
ملف التشغيل:
- ينشئ تطبيق PySide6  
- يستدعي كلاس الواجهة  
- يعرض النافذة  
- يبدأ الحلقة الرئيسية  

### **2️⃣ widget.py**
يحتوي على:
- QLabel لعرض الصورة  
- QPixmap لتحميل الصورة من المسار  
- QVBoxLayout لترتيب الصورة  
- وضع التخطيط داخل النافذة  

---

## 🖼 طريقة تغيير الصورة
ضع الصورة في مجلد المشروع، ثم عدّل السطر التالي:

```python
pixmap = QPixmap("images/my_image.png")
```

بدل وضع مسار مطلق مثل:
```
E:\ML\Application with Pyside\QImage\images\image.png
```

---

## ▶️ طريقة التشغيل
```
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project is a simple **PySide6 image viewer**.  
An image is loaded using `QPixmap` and displayed inside a `QLabel`, organized using a vertical layout.

---

## 📁 Project Structure

### **1️⃣ main.py**
Entry point:
- Creates the QApplication  
- Instantiates the widget  
- Shows the GUI  
- Runs the event loop  

### **2️⃣ widget.py**
Defines the UI:
- QLabel for displaying the image  
- QPixmap for loading it  
- QVBoxLayout to organize the widget  
- Applies the layout to the window  

---

## 🖼 Changing the Image
Place your image inside the project folder and modify:

```python
pixmap = QPixmap("images/my_image.png")
```

---


