import draw.chip as chip
import PIL.Image as I
import PIL.ImageDraw as ID
import numpy as np



if __name__ == '__main__':
    U = 30
    c = chip.element.chip("draw/example/chip1.png", 3*U, 5*U, 4, 5)
    c.add_track(1/4, 1, True, 0)
    c.add_track(2/4, 2, True, 0)
    c.add_track(3/4, 2, True, 1)
    c.add_track(1/4, 1, False, 0)
    c.add_track(2/4, 2, False, 0)
    c.add_track(3/4, 2, False, 1)
    c.save()
