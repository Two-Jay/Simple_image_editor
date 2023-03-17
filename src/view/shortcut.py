from PyQt6.QtCore import Qt
from core.command import (
    Exit_command, Save_command, Open_command
)

class Shortcut_manager():
    @classmethod
    def run_shortcut_command(cls, pressed_key, pressed_modifier):
        if pressed_key == Qt.Key.Key_Escape:
            Exit_command().run()
        if pressed_key == Qt.Key.Key_S and pressed_modifier == Qt.KeyboardModifier.ControlModifier:
            Save_command().run()
        if pressed_key == Qt.Key.Key_O and pressed_modifier == Qt.KeyboardModifier.ControlModifier:
            Open_command().run()