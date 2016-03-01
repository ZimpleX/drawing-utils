"""
directory should be relative to the "draw" package.
"""
from logf.printf import printf
import numpy as np

import PIL.ImageDraw as ID
import PIL.ImageFont as IF
import pdb

def draw_subtree(img_draw, idx, x, y, unit, 
        node_fill="white", tree_fill="blue", 
        node_outline="black", tree_outline="black",
        node_label="", tree_label="",
        n_label_col="black", t_label_col="black"):
    node_r = 0.5*unit
    tri_bottom = 4*unit
    tri_height = 5*unit
    # draw subtree root
    img_draw.ellipse([x-node_r, y-node_r, x+node_r, y+node_r], fill=node_fill, outline=node_outline)
    # draw tree (triangle)
    tri_pts = [0.]*6
    tri_pts[0] = x
    tri_pts[1] = y + node_r
    tri_pts[2] = tri_pts[0] - tri_bottom/2
    tri_pts[3] = tri_pts[1] + tri_height
    tri_pts[4] = tri_pts[0] + tri_bottom/2
    tri_pts[5] = tri_pts[3]
    img_draw.polygon(tri_pts, fill=tree_fill, outline=tree_outline)
    # set macro
    import draw.tree.macro as macro
    macro.subtree_root[idx] = np.array((x,y))
    # add text
    import draw.font as f
    font, _ = f.font_util.adjust_font_size(node_r)
    img_draw.text([x-0.5*node_r, y-0.7*node_r], node_label, fill=n_label_col, font=font)
    
