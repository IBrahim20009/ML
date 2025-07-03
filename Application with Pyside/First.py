# Version#1 of the application , push button
"""from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)
import sys

app = QApplication(sys.argv)

# Window Settings
wind = QMainWindow()
wind.setWindowTitle("Push Button lesson")

# Push Button Settings
button = QPushButton()
button.setText("Press me")
wind.setCentralWidget(button)


wind.show()
app.exec()"""

# Version#2 of the application , make the button as a class 
import sys
import ButtonHolder
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton
)

app = QApplication(sys.argv)
wind = ButtonHolder.PushButton()
wind.show()
app.exec()