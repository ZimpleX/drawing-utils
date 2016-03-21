import draw.misc as misc
import PIL.Image as I
import PIL.ImageDraw as ID
import numpy as np

import pdb


def schedule1():
    U_x = 60
    U_y = 30
    s = misc.job_scheduling.scheduler('draw/example/schedule1.png', U_x, U_y)
    s.add_job(0, 5, 'green')
    s.add_job(1, 3, 'blue')
    s.drawing()
    s.save()





if __name__ == '__main__':
    schedule1()
