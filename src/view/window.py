from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QToolBar, QStatusBar, QMenuBar
)
from PyQt6.QtGui import QIcon, QAction, QPalette, QColor
from PyQt6.QtCore import Qt, QSize
from core.command import Command

import os

class Window(QMainWindow):
    def __init__(self, x=100, y=100, width=500, height=300):
        super(Window, self).__init__()
        self.setWindowTitle("PyQt6")
        self.setGeometry(x, y, width, height)

        self.addToolBar(ToolBar(width, 50))
        self.setStatusBar(QStatusBar(self))

    def keyPressEvent(self, event):
        pressed_key = event.key()
        if pressed_key == Qt.Key.Key_Escape:
            self.close()

class ToolBarButton(QAction):
    def __init__(self, icon, text, callback):
        super(ToolBarButton, self).__init__(icon, text)
        self.setCheckable(True)
        self.triggered.connect(callback)

class ToolBar(QToolBar):
    def __init__(self, width, height):
        super(ToolBar, self).__init__()
        self.setMovable(False)
        self.setFloatable(False)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        
        self.setFixedSize(width, height)
        self.setIconSize(QSize(height - 8, height - 8))

        current_dir = os.getcwd()
        print(f"Current directory: {current_dir + '/resources/icons/save.png'}")

        self.addToolBarButton(
            QIcon(current_dir + "/resources/icons/save.png"),
            "Save",
            self.on_MouseClick
        )
        self.addSeparator()
        self.addToolBarButton(
            QIcon(current_dir + "resources/icons/open.png"),
            "Open",
            self.on_MouseClick
        )



    def addToolBarButton(self, icon, text, callback):
        self.addAction(ToolBarButton(icon, text, callback))

    def on_MouseClick(self):
        print("Clicked")
