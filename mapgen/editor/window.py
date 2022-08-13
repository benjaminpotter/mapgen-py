from PySide6.QtWidgets import QMainWindow

from mapgen.editor.workspace import MGWorkspaceWidget
from mapgen.editor.menu import MGMenuBar

class MGMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Map Gen")

        workspace = MGWorkspaceWidget(parent=self)
        self.setCentralWidget(workspace)

        menu = MGMenuBar(self)
        self.setMenuBar(menu)