from quadtree import QuadTree
from quadtree import TkQuadTree

test = QuadTree.fromFile("files/quadtree.txt")
print(test.bg)
t = TkQuadTree(test.hg, test.hd, test.bg, test.bd)
t.paint()
