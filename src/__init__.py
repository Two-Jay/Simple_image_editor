import sys
from PyQt6.QtWidgets import QApplication
from view.window import Window

def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    return app.exec()

if __name__ == "__main__":
    main()