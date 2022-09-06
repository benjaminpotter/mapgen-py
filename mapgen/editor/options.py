from typing import Optional
from xml.sax.handler import property_declaration_handler

from PySide6.QtWidgets import QWidget, QDockWidget, QPushButton, QHBoxLayout, QFormLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt

from mapgen.generator.map import MapOptions

class MGOptionsDockWidget(QDockWidget):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__("Options", parent, Qt.Widget)

        self.setMinimumWidth(150)
        self.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)

        self.options: MapOptions = MapOptions()

        self.options_menu = QWidget()
        self.options_menu.setLayout(QFormLayout())

        self.resolution_options: QWidget = QWidget(parent=self)
        self.resolution_options.setLayout(QHBoxLayout())
        self.options_menu.layout().addWidget(self.resolution_options)

        self.resolution_options.layout().addWidget(QLabel("Resolution", parent=self))

        self.resolution_width: QLineEdit = QLineEdit(parent=self)
        self.resolution_width.setMaximumWidth(50)
        self.resolution_width.setText(str(self.options.resolution[0]))
        self.resolution_options.layout().addWidget(self.resolution_width)

        self.resolution_options.layout().addWidget(QLabel("x", parent=self))

        self.resolution_height: QLineEdit = QLineEdit(parent=self)
        self.resolution_height.setMaximumWidth(50)
        self.resolution_height.setText(str(self.options.resolution[1]))
        self.resolution_options.layout().addWidget(self.resolution_height)

        self.generateButton = QPushButton("Generate New Map", parent=self)
        self.options_menu.layout().addWidget(self.generateButton)
        
        self.setWidget(self.options_menu)

    @property
    def map_options(self):
        # TODO ensure valid map options?
        self.options.resolution = (int(self.resolution_width.text()), int(self.resolution_height.text()))

        return self.options
        



