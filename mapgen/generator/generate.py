# covers all generation stuffs
from dataclasses import dataclass
from noise import pnoise2
from random import randint, random
from typing import List
import math

from mapgen.utils import map_to_range
from mapgen.generator.map import Map, MapOptions

class Generator():

    @staticmethod
    def _perlin(x: float, y: float, offset: int):
        """
        Returns noise at [x, y]
        """

        # TODO apply noise layering

        noise = pnoise2(x, y, base=offset, octaves=6)
        return map_to_range(noise, -math.sqrt(2)/2, math.sqrt(2)/2, 0, 1)

    @staticmethod
    def _generate_noise(resolution: tuple) -> List:
        """
        Generates noise map. Data returned is a list of lists where the nested lists are rows.
        In each row there are floating point values from 0-1 that represent terrain height.
        """

        seed = randint(0, 100)
        
        noise_map = [None] * resolution[1]
        for y in range(resolution[1]):
            row = [0] * resolution[0]
            for x in range(resolution[0]):

                xn = map_to_range(x, 0, resolution[0], 0, 1)
                yn = map_to_range(y, 0, resolution[1], 0, 1)

                row[x] = Generator._perlin(xn, yn, seed)
                
            noise_map[y] = row

        return noise_map

    @staticmethod
    def generate(opts: MapOptions) -> Map:
        """
        Generate and return a full map object.

        TODO spawn a new thread
        """

        map = Map(noise_map=Generator._generate_noise(opts.resolution))
        return map


   