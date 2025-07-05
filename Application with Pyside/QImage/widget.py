from PySide6.QtWidgets import QLabel, QWidget , QVBoxLayout
from PySide6.QtGui import QPixmap

class widget(QWidget):
    def __init__(self):
        super().__init__()
        image = QLabel()
        pixmap = QPixmap(r"E:\ML\Application with Pyside\QImage\images\image.png")
        image.setPixmap(pixmap)

        v_layout = QVBoxLayout()
        v_layout.addWidget(image)

        self.setLayout(v_layout)
