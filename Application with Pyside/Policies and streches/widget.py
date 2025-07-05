from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QSizePolicy, QHBoxLayout

class widget(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("Some text :")
        line_edit =  QLineEdit()

        line_edit.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Fixed)
        
        layout = QHBoxLayout()
        layout.addWidget(label,1)
        layout.addWidget(line_edit,10)
        self.setLayout(layout)