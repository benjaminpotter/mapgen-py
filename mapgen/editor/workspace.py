from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog

from mapgen.editor.map import MGMapGraphicsItem
from mapgen.generator.generate import Generator, NoiseMapProcessingData

from mapgen import utils


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

    def save_map(self):
        filepath = QFileDialog.getSaveFileName(self, caption="Export to PNG", filter="Images (*.png)", dir="/")[0] # for some reason this returns a tuple with the filter
        if filepath == "": # if the user cancels
            return

        print(f"Saving map to {filepath}...")

        img = utils.flatten_list((300, 300), self.map_item.image)

        utils.write_to_png(
            filepath, 
            (300, 300), # self.map_item.extents
            img
        )