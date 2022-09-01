from typing import List
from dataclasses import dataclass

@dataclass 
class MapOptions:
    resolution: tuple = (500, 500)

    roughness: int = 0

@dataclass
class MapDisplayOptions:
    sea_level: int = 0.5
    # etc...


class Map:
    """
    Responsible for maintaining data about a map. Should not mutate the data about itself.
    """

    def __init__(self, noise_map: List = None, display_opts: MapDisplayOptions = MapDisplayOptions()):
        
        self._colour = None
        self._greyscale = None

        self.noise_map = noise_map
        self.width = 0
        self.height = 0

        self.display_opts = display_opts

        if noise_map is not None:
            self.width = len(self.noise_map[0])
            self.height = len(self.noise_map)

    @property
    def resolution(self) -> tuple:
        return (self.width, self.height)

    @property
    def colour(self) -> List:
        if self._colour is None:
            image = [None] * self.height
            for y in range(self.height):
                row = [0] * self.width
                for x in range(self.width):
                    noise = self.noise_map[x][y]
                    row[x] = (0, 255, 0)
                    if noise < self.display_opts.sea_level: # TODO set options
                        row[x] = (0, 0, 255)
                    
                image[y] = row
                    
            self._colour = image

        return self._colour

    @property
    def greyscale(self) -> List:
        if self._greyscale is None:
            image = [None] * self.height
            for y in range(self.height):
                row = [0] * self.width
                for x in range(self.width):
                    noise_col = self.noise_map[y][x] * 255.0
                    row[x] = [noise_col] * 3
                image[y] = row
                
            self._greyscale = image

        return self._greyscale