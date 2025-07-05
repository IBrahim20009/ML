from PySide6.QtWidgets import QApplication 
from Widget import window
import sys

app = QApplication(sys.argv)
wind = window()
wind.show()
app.exec()
