from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QToolBar, QStatusBar, QMenuBar
)
from PyQt6.QtGui import QIcon, QAction, QPalette, QColor
from PyQt6.QtCore import Qt, QSize
from view.shortcut import Shortcut_manager
from core.command import (
    Save_command, Open_command
)

import os

class Window(QMainWindow):
    def __init__(self, x=100, y=100, width=500, height=300):
        super(Window, self).__init__()
        self.setWindowTitle("simple image editor")
        self.setGeometry(x, y, width, height)

        self.addToolBar(ToolBar(width, 50))
        self.setStatusBar(QStatusBar(self))

    def keyPressEvent(self, event):
        Shortcut_manager.run_shortcut_command(event.key(), event.modifiers())

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
        
        self.setFixedSize(width, height)
        self.setIconSize(QSize(height - 8, height - 8))

        current_dir = os.getcwd()
        image_folder_path = os.path.join(current_dir, "resources/icons")
        print(f"image_folder_path : {image_folder_path}")

        self.addToolBarButton(
            QIcon(image_folder_path + "/save.png"),
            "Save",
            Save_command().run
        )
        self.addSeparator()
        self.addToolBarButton(
            QIcon(image_folder_path + "/open.png"),
            "Open",
            Open_command().run
        )
        self.addSeparator()

    def addToolBarButton(self, icon, text, callback):
        self.addAction(ToolBarButton(icon, text, callback))