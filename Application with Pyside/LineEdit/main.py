from PySide6.QtWidgets import QApplication
from widget import widget
import sys
app = QApplication(sys.argv)
wind = widget()
wind.show()
app.exec()