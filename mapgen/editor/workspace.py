from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog

from mapgen.editor.map_display import MGMapGraphicsItem
from mapgen.generator.generate import Generator

from mapgen import utils
from mapgen.generator.map import Map, MapOptions


class MGWorkspaceWidget(QGraphicsView):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setScene(QGraphicsScene(self))

        self.resolution = (300, 300) # can't handle large maps...
        
        self.map: Map = None
        self.map_display = MGMapGraphicsItem()
        self.scene().addItem(self.map_display)
        
        self.refresh_map()

    def refresh_map(self):
        
        opts = MapOptions() # use defaults for now

        self.map = Generator.generate(opts)
        self.map_display.set_map_image(self.map.colour)

    def save_map(self):
        filepath = QFileDialog.getSaveFileName(self, caption="Export to PNG", filter="Images (*.png)", dir="/")[0] # for some reason this returns a tuple with the filter
        if filepath == "": # if the user cancels
            return

        print(f"Saving map to {filepath}...")
        img = utils.flatten_list(self.map.resolution, self.map.colour)
        utils.write_to_png(filepath, self.map.resolution, img)