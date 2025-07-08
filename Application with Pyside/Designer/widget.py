from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        self.ui = loader.load(r"E:\ML\Application with Pyside\Designer\untitled.ui",None)
        self.ui.setWindowTitle("User data")
        self.ui.Submit.clicked.connect(self.dosomething)
    def show(self):
        self.ui.show()
    def dosomething(self):
        print(self.ui.lineEditForFullname.text(),"is a ", self.ui.lineEditForRole.text())
