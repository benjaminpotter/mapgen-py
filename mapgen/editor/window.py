from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from mapgen.editor.workspace import MGWorkspaceWidget
from mapgen.editor.menu import MGMenuBar
from mapgen.editor.options import MGOptionsDockWidget

class MGMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MapGenPy")

        self.workspace = MGWorkspaceWidget(parent=self)
        self.setCentralWidget(self.workspace)

        menu = MGMenuBar(self, self.workspace)
        self.setMenuBar(menu)

        options = MGOptionsDockWidget(parent=self)
        options.generateButton.clicked.connect(lambda: self.workspace.refresh_map(options.map_options))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, options)