# Introduction to PySide
تعريف عن PySide

---

## 📌 What is PySide?  
**PySide** is the official Python module for the **Qt framework**, used to build professional and cross-platform desktop applications.  
PySide provides Python bindings for Qt, allowing developers to create rich GUIs with ease.

**PySide** هو المكتبة الرسمية لربط لغة **بايثون** مع إطار العمل **Qt**، والمستخدم في تطوير تطبيقات سطح مكتب احترافية ومتعددة المنصات.  
توفر PySide أدوات قوية لإنشاء واجهات رسومية بسهولة وبمرونة عالية.

---

## 🧩 PySide vs PyQt  
Both PySide and PyQt are Python bindings for Qt.  
However:

| Feature | PySide | PyQt |
|--------|--------|-------|
| License | LGPL | GPL / Commercial |
| Maintained by | Qt Company | Riverbank |
| Ease of use | ✔ | ✔ |
| Open Source friendly | ✔ | – |

الاختلاف الأساسي أن **PySide** مناسب للمشاريع المفتوحة والخاصّة بدون قيود الترخيص.

---

## 🎨 Building UI with Qt Designer  
PySide supports `.ui` files created with **Qt Designer**.  
These files can be converted to Python using:

```bash
pyside6-uic interface.ui -o interface.py
