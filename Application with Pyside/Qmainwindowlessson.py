from PySide6.QtWidgets import QMainWindow, QToolBar , QPushButton, QStatusBar
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize 

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Main Window")
        menu_bar= self.menuBar()
        file_menu = menu_bar.addMenu("&File") 
        Quit= file_menu.addAction("Quit")
        Quit.setStatusTip("To shut down the app")
        Quit.triggered.connect(self.QUIT)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        toolbar.addAction(Quit)

        action1 = QAction("Some Action",self)
        action1.setStatusTip("Status massage for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here !!!")).setStatusTip("Nothing here")
        
        # Status bar 
        self.setStatusBar(QStatusBar(self))

        button = QPushButton("Button1")
        button.clicked.connect(self.button1)
        self.setCentralWidget(button)

    def button1(self):
        print("hi from button 1")


    def QUIT(self):
        self.app.quit()
    def toolbar_button_click(self):
        print("Hi there")
    def Statusbar(self):
        self.statusBar().showMessage("Hi there from Status bar ",3)