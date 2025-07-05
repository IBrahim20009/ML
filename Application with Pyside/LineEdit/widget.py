from PySide6.QtWidgets import QWidget, QHBoxLayout , QVBoxLayout , QLabel , QPushButton , QLineEdit

class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line Edit")

        Label = QLabel("Enter the full name: ")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.textchanges)

        button =  QPushButton("Grab data")
        button.clicked.connect(self.GrabData)
        self.text_holder_label = QLabel("I AM HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(Label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)


    def GrabData(self):
        # print(f"Full name is : {self.line_edit.text()}")
        self.text_holder_label.setText(self.line_edit.text())
    def textchanges(self):
        self.text_holder_label.setText(self.line_edit.text())