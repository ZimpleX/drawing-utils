from logf.printf import printf
import numpy as np

import PIL.Image as I
import PIL.ImageDraw as ID
import PIL.ImageFont as IF
import pdb


class chip:
    def __init__(self, img_out, clb_wid, chan_wid, row, col):
        self.img_out = img_out
        self.clb_wid = clb_wid
        self.chan_wid = chan_wid
        self.row = row
        self.col = col
        self.W = col*(clb_wid+chan_wid) + chan_wid
        self.H = row*(clb_wid+chan_wid) + chan_wid
        self.img = I.new('RGB', (self.W, self.H), "white")
        self.draw = ID.Draw(self.img)
        for r in range(self.row):
            for c in range(self.col):
                x = self.chan_wid + c*(self.chan_wid + self.clb_wid)
                y = self.chan_wid + r*(self.chan_wid + self.clb_wid)
                self.draw.rectangle([x,y,x+self.clb_wid,y+self.clb_wid],outline='black')
    def add_track(self, track_fraction, wlen, is_x_dir, start_clb):
        """
        start_clb index starts from 0
        """
        if is_x_dir:
            for r in range(self.row-1):
                y = (r+1)*(self.chan_wid+self.clb_wid) + track_fraction*self.chan_wid
                for c in range(start_clb, self.col, wlen):
                    x0 = self.chan_wid + (self.chan_wid+self.clb_wid)*c
                    x1 = x0 + wlen*self.clb_wid + (wlen-1)*self.chan_wid
                    x1 = min(self.W-self.chan_wid, x1)
                    self.draw.line([x0,y,x1,y], fill="black")
                if start_clb > 0:
                    x0 = self.chan_wid
                    x1 = x0 + start_clb*self.clb_wid + (start_clb-1)*self.chan_wid
                    self.draw.line([x0,y,x1,y], fill="black")
        else:
            for c in range(self.col-1):
                x = (c+1)*(self.chan_wid+self.clb_wid) + track_fraction*self.chan_wid
                for r in range(start_clb, self.row, wlen):
                    y0 = self.chan_wid + (self.chan_wid+self.clb_wid)*r
                    y1 = y0 + wlen*self.clb_wid + (wlen-1)*self.chan_wid
                    y1 = min(self.H-self.chan_wid, y1)
                    self.draw.line([x,y0,x,y1], fill='black')
                if start_clb > 0:
                    y0 = self.chan_wid
                    y1 = y0 + start_clb*self.clb_wid + (start_clb-1)*self.chan_wid
                    self.draw.line([x,y0,x,y1], fill='black')   
                
    

    def save(self):
        self.img.save(self.img_out, "PNG")
