from PyQt6.QtCore import Qt
from core.command import Command

class Shortcut_manager():
    @classmethod
    def run_shortcut_command(cls, pressed_key, pressed_modifier):
        if pressed_key == Qt.Key.Key_Escape:
            Command("escape").run()
        if pressed_key == Qt.Key.Key_S and pressed_modifier == Qt.KeyboardModifier.ControlModifier:
            Command("save").run()
        if pressed_key == Qt.Key.Key_O and pressed_modifier == Qt.KeyboardModifier.ControlModifier:
            Command("open").run()