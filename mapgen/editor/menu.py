from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QAction

from mapgen.editor.workspace import MGWorkspaceWidget

class MGMenuBar(QMenuBar):

  def __init__(self, parent, workspace):
    super().__init__(parent)

    self.workspace: MGWorkspaceWidget = workspace

    file = QMenu("File", self)

    actionExport = QAction("&Export", self)
    actionExport.triggered.connect(self.workspace.save_map)

    file.addAction(actionExport)
    self.addMenu(file)

