from PySide6.QtWidgets import (
    QWidget,
    QCheckBox,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QButtonGroup,
    QRadioButton)
class widget(QWidget):
    def __init__(self):
        super().__init__()

        os = QGroupBox("Chose the OS :")
        windows = QRadioButton("Windows")
        windows.toggled.connect(self.print)
        
        linux = QRadioButton("Linux")
        linux.toggled.connect(self.printforlinux)
        
        windows.setChecked(True)
        ss= QButtonGroup(self)
        ss.addButton(windows)
        ss.addButton(linux)
        ss.setExclusive(True)

        layout =  QHBoxLayout()
        layout.addWidget(linux)
        layout.addWidget(windows)
        self.setLayout(layout)
    def print(self):
        print("hj")

    def printforlinux(self):
        print("hi from linux")