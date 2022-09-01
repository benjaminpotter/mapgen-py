from typing import List, Tuple
from PIL import Image

def flatten_list(size: Tuple, list: List):
    out = []
    for x in range(size[0]):
        for y in range(size[1]):
            out.append(list[x][y])

    return out

def write_to_png(filepath: str, size: Tuple, data: List):
    img = Image.new("RGB", size)
    img.putdata(data=data)

    img.save(filepath)

def map_to_range(val, ilb, itb, olb, otb):
    return olb + ((otb - olb) / (itb - ilb)) * (val - ilb)