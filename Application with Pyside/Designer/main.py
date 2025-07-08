import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader 
from widget import UserInterface
loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = UserInterface()

window.show()
app.exec()