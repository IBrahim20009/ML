from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
import sys

class UploadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Upload Button Example")
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("No file selected")
        self.upload_button = QPushButton("Upload File")
        self.upload_button.clicked.connect(self.upload_file)
        self.upload_button.setStyleSheet("color: white; background-color: #169C96; font-weight: bold;")

        layout.addWidget(self.upload_button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a file")
        if file_path:
            self.label.setText(f"Selected: {file_path}")
        else:
            self.label.setText("No file selected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UploadWindow()
    window.show()
    sys.exit(app.exec())
