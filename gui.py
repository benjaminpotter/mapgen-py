import sys

from PySide6.QtWidgets import QApplication
from mapgen.editor.window import MGMainWindow

if __name__ == "__main__":
    app = QApplication([])

    mainWindow = MGMainWindow()
    mainWindow.resize(800, 600)
    mainWindow.show()

    sys.exit(app.exec())

