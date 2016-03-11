import draw.chip as chip
import PIL.Image as I
import PIL.ImageDraw as ID
import numpy as np



if __name__ == '__main__':
    U = 30
    c = chip.element.chip("draw/example/chip1.png", 3*U, 5*U, 3, 4)
    c.add_track(1/4, 1, True, 0)
    c.add_track(2/4, 2, True, 0)
    c.add_track(3/4, 2, True, 1)
    c.add_track(1/4, 1, False, 0)
    c.add_track(2/4, 2, False, 0)
    c.add_track(3/4, 2, False, 1)
    
    c.label_clb(0,1,'MUL')
    c.label_clb(1,2,'MUL')
    c.label_clb(2,3,'MUL')

    c.sig_flow(0.5,0)
    c.connect_pin(0.5,0,0,1)

    c.sig_flow(1.5,0)
    c.sig_flow(1.25,2)
    c.connect(1.5,0,1.25,2)
    c.connect_pin(1.25,2,1,2)

    c.sig_flow(1.75,0)
    c.sig_flow(1.75,1)
    c.sig_flow(1.75,3)
    c.connect(1.75,0,1.75,1)
    c.connect(1.75,1,1.75,3)
    c.connect_pin(1.75,3,2,3)

    c.label_sig(0.5,0,'A[0]',fill='red')
    c.label_sig(1.5,0,'A[1]',fill='red')
    c.label_sig(1.75,0,'A[2]',fill='red')
    
    c.sig_flow(0,0.75,fill='blue')
    c.connect_pin(0,0.75,0,1,fill='blue')
    c.sig_flow(0,1.5,fill='blue')
    c.connect_pin(0,1.5,1,2,fill='blue')
    c.sig_flow(0,2.5,fill='blue')
    c.sig_flow(2,2.5,fill='blue')
    c.connect(0,2.5,2,2.5,fill='blue')
    c.connect_pin(2,2.5,2,3,fill='blue')

    c.label_sig(0,0.75,'k',fill='blue')
    c.label_sig(0,1.5,'k',fill='blue')
    c.label_sig(0,2.5,'k',fill='blue')

    c.save()
