import draw.tree as tree
import PIL.Image as I
import PIL.ImageDraw as ID
import numpy as np

def graph1(unit):
    W = 10*unit
    H = 7*unit
    img = I.new("RGB", (W,H), "white")
    draw = ID.Draw(img)
    nodes = [[0.6*W, 0.15*H]]
    nodes+= [[0.55*W, 0.55*H]]
    nodes+= [[0.15*W, 0.8*H]]
    nodes+= [[0.85*W, 0.7*H]]
    idx = 0
    for n in nodes:
        tree.element.draw_node(draw, idx, n[0],n[1], unit, label=str(idx))
        idx += 1 
    conns = [[(0,1), "1"]]
    conns+= [[(1,2), "3"]]
    conns+= [[(1,3), "100"]]
    conns+= [[(0,3), "2"]]
    conns+= [[(0,2), "101"]]
    idx = 0
    for c in conns:
        tree.connect.connect_nodes(draw, c[0][0],c[0][1], unit, label=c[1])
        idx += 1

    img.save("draw/example/graph1.png", "PNG")


if __name__ == "__main__":
    graph1(30)
