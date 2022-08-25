# covers all generation stuffs
from dataclasses import dataclass
from noise import pnoise2
from random import randint, random
from typing import List

@dataclass
class NoiseMapProcessingData:
    sea_level: float
    # etc...

class Generator():

    @staticmethod
    def generate_noise(resolution: tuple) -> List: # signature will be extended in the future
        print("Generating...")

        #pnoise = PerlinNoise(octaves=3, seed=1)
        maxs = []
        seed = randint(0, 100)

        noise_map = [None] * resolution[1]
        for y in range(resolution[1]):
            row = [0] * resolution[0]
            for x in range(resolution[0]):
                row[x] = (pnoise2(x/resolution[0], y/resolution[1], octaves=12, base=seed) / 0.7 + 1.0) / 2.0
                
            maxs.append(max(row))
            noise_map[y] = row

        return noise_map


    @staticmethod
    def noise_to_greyscale(noise_map: List) -> List:
        """
        Convert noisemap to a RGB greyscale image.
        """

        # check for invalid noise map

        width = len(noise_map[0])
        height = len(noise_map)

        image = [None] * height
        for y in range(height):
            row = [0] * width
            for x in range(width):
                noise_col = noise_map[y][x] * 255.0
                row[x] = [noise_col] * 3
            image[y] = row
                
        return image


    @staticmethod
    def noise_to_pixels(noise_map: List, processing_data: NoiseMapProcessingData) -> List:
        """
        Takes noise map (List of floating points between 0-1) and converts it to a colour image
        """

        width = len(noise_map[0])
        height = len(noise_map)

        image = [None] * height
        for y in range(height):
            row = [0] * width
            for x in range(width):
                noise = noise_map[y][x]
                row[x] = (0, 255, 0)
                if noise < processing_data.sea_level:
                    row[x] = (0, 0, 255)
                
            image[y] = row
                
        return image