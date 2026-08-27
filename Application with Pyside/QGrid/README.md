# PySide6 Grid Layout Demo — شرح + Documentation  
(English version below)

---

## 🇸🇦 الشرح بالعربي

هذا المشروع يوضّح كيفية استخدام **QGridLayout** في PySide6 لتنظيم العناصر داخل واجهة رسومية على شكل شبكة (Grid).

الواجهة تحتوي على 9 أزرار موزعة داخل شبكة 3 × 3.

### ✔ مميزات الواجهة:
- استخدام التخطيط الجدولي Grid Layout
- إضافة أزرار متعددة
- توضيح مفهوم **Row / Column / RowSpan / ColumnSpan**

### 📌 توزيع الأزرار:
```
Button 1 | Button 2 | Button 3
Button 4 | Button 5 | Button 6
Button 7 | Button 8 | Button 9
```

حيث أن:
- Button 1 يمتد على عمودين (ColumnSpan = 2)

---

## 📁 ملفات المشروع

### **1️⃣ main.py**
يشغّل التطبيق:
- ينشئ `QApplication`
- يستدعي نافذة الواجهة
- يعرض النافذة
- يبدأ الحلقة الرئيسية

### **2️⃣ widget.py**
يحتوي على:
- 9 أزرار
- تخطيط Grid Layout
- استخدام امتداد الأعمدة (ColumnSpan)

---

## ▶️ طريقة التشغيل
```bash
python3 main.py
```

---

# 🇺🇸 English Documentation

## Overview
This project demonstrates how to use **QGridLayout** in PySide6 to arrange widgets in a table-like structure.

The UI contains **9 buttons** arranged in a 3×3 grid.

### ✔ Key Layout Concepts:
- Grid organization (rows and columns)
- Adding multiple buttons
- Using **rowSpan** and **columnSpan**

### 📌 Grid Layout Structure:
```
Button 1 | Button 2 | Button 3
Button 4 | Button 5 | Button 6
Button 7 | Button 8 | Button 9
```

Note:  
Button 1 spans **two columns**, showing how column spanning works.

---

## 📁 Project Structure

### **1️⃣ main.py**
Entry point:
- Creates QApplication  
- Instantiates the window  
- Displays it  
- Starts the event loop  

### **2️⃣ widget.py**
Defines the UI:
- 9 QPushButtons  
- Positioned using QGridLayout  
- Example of column spanning for Button 1  

---


