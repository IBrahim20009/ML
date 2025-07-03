from PySide6.QtWidgets import QPushButton, QVBoxLayout,QHBoxLayout, QWidget
class RockWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widgets")

        CKDButton = QPushButton("CKD")
        CKDButton.clicked.connect(self.CKD)

        HypertensionButton = QPushButton("Hypertension")
        HypertensionButton.clicked.connect(self.Hypertension)

        Layout = QHBoxLayout()


        Layout.addWidget(CKDButton)
        Layout.addWidget(HypertensionButton)
        
        self.setLayout(Layout)



    def Hypertension(self):
        print("Hypertension button has been clicked.")


    def CKD(self):
        print("CKD button has been clicked.")

