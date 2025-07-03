from  PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # Push button for hard 
        hardbutton = QPushButton("Hard")
        hardbutton.clicked.connect(self.hardfunc)
        # Push button for critical 
        criticalbutton = QPushButton("critical")
        criticalbutton.clicked.connect(self.criticalfunc)
        # Push button for Question
        Questionbutton = QPushButton("Question")
        Questionbutton.clicked.connect(self.Questionfunc)
        # Push button for Information 
        Informationbutton = QPushButton("Information")
        Informationbutton.clicked.connect(self.Informationfunc)
        # Push button for Warning 
        Warningbutton = QPushButton("Warning")
        Warningbutton.clicked.connect(self.Warningfunc)


        # Layout for the buttons 
        layout = QVBoxLayout()
        layout.addWidget(hardbutton)
        layout.addWidget(criticalbutton)
        layout.addWidget(Questionbutton)
        layout.addWidget(Informationbutton)
        layout.addWidget(Warningbutton)
        self.setLayout(layout)
    def hardfunc(self):
        ret = QMessageBox.critical(self, "Message title",
                                   "Critical Message",
                                    QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            print("Ok selected")
        else:
            print("nothing selected")
    def criticalfunc(self):
        print("Critical")
    def Informationfunc(self):
        print("Information")
    def Questionfunc(self):
        print("Question")
    def Warningfunc(self):
        print("Warning")