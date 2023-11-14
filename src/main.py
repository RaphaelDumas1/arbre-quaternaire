from quadtree import QuadTree
from quadtree import TkQuadTree

quadtree = QuadTree.fromFile("files/quadtree.txt")
quadtreeUI = TkQuadTree(quadtree.hg, quadtree.hd, quadtree.bd, quadtree.bg)
quadtreeUI.paint()
