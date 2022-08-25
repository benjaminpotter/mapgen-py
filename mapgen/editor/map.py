from typing import List, Optional
from PySide6.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QRectF, QSizeF, QPointF

class MGMapGraphicsItem(QGraphicsItem):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.width = 0
        self.height = 0

        self.map_image: List = None

    @property
    def extents(self) -> QSizeF:
        return QSizeF(self.width, self.height)
    
    def set_map_image(self, map_image: List):
        
        # verify map_image
        self.map_image = map_image

        self.width = len(map_image[0])
        self.height = len(map_image)
        
        self.update()

    def boundingRect(self) -> QRectF:
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        if self.map_image == None:
            painter.drawRect(0, 0, 100, 100)
            painter.drawText(10, 50, "No image.")
            return
        
        for y in range(self.height):
            for x in range(self.width):
                painter.setPen(QColor(
                    self.map_image[y][x][0], 
                    self.map_image[y][x][1], 
                    self.map_image[y][x][2])
                    )
                painter.drawPoint(x, y)