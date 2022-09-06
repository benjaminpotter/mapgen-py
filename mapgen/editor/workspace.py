from typing import Union

from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog
from PySide6.QtCore import QRectF, QRect
from PySide6.QtGui import QPainter, QColor

from mapgen.editor.map_display import MGMapGraphicsItem
from mapgen.generator.generate import Generator
from mapgen import utils
from mapgen.generator.map import Map, MapOptions


class MGGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

    def drawBackground(self, painter: QPainter, rect: Union[QRectF, QRect]) -> None:
        painter.fillRect(rect, QColor(200, 200, 200))


class MGWorkspaceWidget(QGraphicsView):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setScene(QGraphicsScene(self))
        
        self.map: Map = None
        self.map_display = MGMapGraphicsItem()
        self.scene().addItem(self.map_display)
        
        # self.refresh_map(MapOptions())

    def refresh_map(self, opts: MapOptions):
        self.map = Generator.generate(opts)

        self.scene().update() # redraw background
        self.map_display.set_map_image(self.map.colour)

    def save_map(self):
        filepath = QFileDialog.getSaveFileName(self, caption="Export to PNG", filter="Images (*.png)", dir="/")[0] # for some reason this returns a tuple with the filter
        if filepath == "": # if the user cancels
            return

        print(f"Saving map to {filepath}...")
        img = utils.flatten_list(self.map.resolution, self.map.colour)
        utils.write_to_png(filepath, self.map.resolution, img)