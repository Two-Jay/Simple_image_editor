from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QToolBar, QStatusBar, QMenuBar
)
from PyQt6.QtGui import QIcon, QAction, QPalette, QColor
from PyQt6.QtCore import Qt, QSize
from view.shortcut import Shortcut_manager
from core.command import Command

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
        print(f"Current directory: {current_dir + '/resources/icons/save.png'}")

        self.addToolBarButton(
            QIcon(image_folder_path + "/save.png"),
            "Save",
            Command("save").run
        )
        self.addSeparator()
        self.addToolBarButton(
            QIcon(image_folder_path + "/open.png"),
            "Open",
            Command("open").run
        )
        self.addSeparator()
        self.addToolBarButton(
            QIcon(image_folder_path + "/zoomin.png"),
            "Zoom in",
            Command("zoomin").run
        )
        self.addToolBarButton(
            QIcon(image_folder_path + "/zoomout.png"),
            "Zoom out",
            Command("zoomout").run
        )
        self.addToolBarButton(
            QIcon(image_folder_path + "/rotate_toolbar.png"),
            "Rotate",
            Command("rotate").run
        )
        self.addSeparator()

    def addToolBarButton(self, icon, text, callback):
        self.addAction(ToolBarButton(icon, text, callback))