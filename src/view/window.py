from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyQt6")
        self.setGeometry(100, 100, 500, 300)

        self.addToolBar(ToolBar())

class ToolBar(QToolBar):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.setMovable(False)
        self.setFloatable(False)
        self.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)