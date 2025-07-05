from PySide6.QtWidgets import QWidget , QPushButton, QVBoxLayout , QMessageBox

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("I dont know what to title it")
        button = QPushButton("Let see what is the signal")
        button.clicked.connect(self.click)
        button.pressed.connect(self.press)
        button.released.connect(self.release)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def click(self):
        print("Clicked")
    def press(self):
        print("Pressed")
    def release(self):
        print("Released")