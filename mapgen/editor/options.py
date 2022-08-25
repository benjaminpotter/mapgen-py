from typing import Optional

from PySide6.QtWidgets import QWidget, QDockWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class MGOptionsDockWidget(QDockWidget):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__("Options", parent, Qt.Widget)

        self.setMinimumWidth(150)
        self.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)

        self.optionsMenu = QWidget()
        self.optionsMenu.setLayout(QHBoxLayout())

        self.generateButton = QPushButton("Generate New Map", parent=self)
        self.optionsMenu.layout().addWidget(self.generateButton)
        
        self.setWidget(self.optionsMenu)

        # wire signals
        # self.generateButton.clicked.connect(self.parentWidget().refresh_map)
        



