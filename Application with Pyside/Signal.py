# Version 1 
"""from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

app = QApplication()
wind = QMainWindow()

def GiveInfo(data):
    print(f"The Bool Value is: {data}")
button = QPushButton("Press me!")
button.setCheckable(True)
button.clicked.connect(GiveInfo)
wind.setCentralWidget(button)
wind.show()
app.exec()"""

# Version 2
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication , QSlider
def response_to_slider(data):
    print(f"Silder moved to : {data}")

app = QApplication()
silder= QSlider(Qt.Horizontal)
silder.setMinimum(1)
silder.setMaximum(100)
silder.setValue(1)

silder.valueChanged.connect(response_to_slider)
silder.show()
app.exec()
