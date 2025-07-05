from widget import window
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

wind = window()
wind.show()
app.exec()