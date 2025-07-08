from PySide6.QtWidgets import QWidget , QComboBox,QPushButton, QVBoxLayout

class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.combo = QComboBox(self)
        self.combo.addItem("hyper")
        self.combo.addItem("CKD")

        but1 = QPushButton("Current value")
        but1.clicked.connect(self.Currentvalue)
        but2 = QPushButton("set value")
        but2.clicked.connect(self.setcurrent)
        but3 = QPushButton("get value")
        but3.clicked.connect(self.getvalues)

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(but1)
        layout.addWidget(but2)
        layout.addWidget(but3)
        self.setLayout(layout)

    def Currentvalue(self):
        print(f"Current item : {self.combo.currentText()} , index {self.combo.currentIndex()}")
        if self.combo.currentText() == "CKD":
            print("CKD model")
        elif self.combo.currentText() == "hyper":
            print("Hyper model")
    def setcurrent(self):
        self.combo.setCurrentIndex(1)
    def getvalues(self):
        for i in range(self.combo.count()):
            print(f"index [{i}] , {self.combo.itemText(i)}")