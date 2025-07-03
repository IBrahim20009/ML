from qwidgets import RockWidgets
import sys 
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
widget = RockWidgets()
widget.show()
app.exec()