from Qmainwindowlessson import MainWindow
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

wind = MainWindow(app)
wind.show()
app.exec()