# PySide6 Desktop Example  
Simple GUI with Radio Buttons (Windows / Linux)

# مثال PySide6  
واجهة بسيطة تحتوي على خيارات نظام التشغيل (ويندوز / لينكس)

---

## 📌 Overview | نظرة عامة

This project is a simple PySide6 desktop application demonstrating how to use **Radio Buttons**, **signals**, and **layouts** in a Python GUI.

يعرض هذا المشروع مثالًا بسيطًا لتطبيق PySide6 يوضّح كيفية استخدام **أزرار الاختيار (Radio Buttons)**، والإشارات (Signals)، وترتيب العناصر داخل الواجهة.

---

# 🗂 File Explanation | شرح الملفات

## 1️⃣ main.py

### **English Explanation**
`main.py` is the entry point of the application. It:
- Creates a `QApplication`
- Imports the main widget from `Widget.py`
- Shows the window
- Runs the event loop using `app.exec()`

### **Arabic Explanation**
ملف **main.py** هو نقطة التشغيل الأساسية للتطبيق، حيث:
- ينشئ كائن `QApplication`
- يستورد الواجهة الرئيسية من `Widget.py`
- يعرض نافذة التطبيق
- يبدأ حلقة التشغيل باستخدام `app.exec()`

### **Code**
```python
from PySide6.QtWidgets import QApplication
from Widget import widget
import sys 

app = QApplication(sys.argv)
wind = widget()
wind.show()
app.exec()
