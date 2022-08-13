from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from PySide6.QtCore import QRectF
from PySide6.QtGui import QColor

class MGWorkspaceWidget(QGraphicsView):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setScene(QGraphicsScene(self))
        self.drawTestCircle()
        
    def drawTestCircle(self):
        self.scene().addEllipse(QRectF(400, 300, 100, 100), QColor(0, 0, 0), QColor(0, 0, 0))
