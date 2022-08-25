from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from PySide6.QtCore import QRectF
from PySide6.QtGui import QColor

from mapgen.editor.map import MGMapGraphicsItem
from mapgen.generator.generate import Generator, NoiseMapProcessingData


class MGWorkspaceWidget(QGraphicsView):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setScene(QGraphicsScene(self))
        
        self.map_item = MGMapGraphicsItem()
        self.scene().addItem(self.map_item)
        
        self.refresh_map()

    def refresh_map(self): # TODO where should this happen?
        
        noise_map = Generator.generate_noise((300, 300))
        # image = Generator.noise_to_greyscale(noise_map)
        image = Generator.noise_to_pixels(noise_map, NoiseMapProcessingData(0.5))

        self.map_item.set_map_image(image)