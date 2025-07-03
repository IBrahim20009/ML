from PySide6.QtWidgets import QMainWindow, QPushButton

class PushButton(QMainWindow):
    def __init__(self):
        super.__init__()
        button = QPushButton("Press me ")

        self.setCentralWidget(button)