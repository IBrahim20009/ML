from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout



class window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        self.buttons = []

        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")
        btn5 = QPushButton("Button 5")
        btn6 = QPushButton("Button 6")
        btn7 = QPushButton("Button 7")
        btn8 = QPushButton("Button 8")
        btn9 = QPushButton("Button 9")

        layout.addWidget(btn1, 0, 0,1,2)
        layout.addWidget(btn2, 0, 1)
        layout.addWidget(btn3, 0, 2)
        layout.addWidget(btn4, 1, 0)
        layout.addWidget(btn5, 1, 1)
        layout.addWidget(btn6, 1, 2)
        layout.addWidget(btn7, 2, 0)
        layout.addWidget(btn8, 2, 1)
        layout.addWidget(btn9, 2, 2)
