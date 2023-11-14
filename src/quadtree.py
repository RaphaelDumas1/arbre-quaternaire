from __future__ import annotations
from tkinter import *

class QuadTree:
    NB_NODES : int = 4
    _depth : int = 0

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        return self._depth

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """Returns a Quadtree object from a file which must contains list [] and 0 or 1 representing the shape of the tree"""
        """(I know there is a native function to do that :D)"""
        saveList = []
        depth = 0
        list = None
        with open(filename, 'r') as file:
            char = file.read(1)
            while char:
                if(len(saveList) != 0):
                    list = saveList[depth - 1]    
                elif(list == None):
                    list = []

                if(char == '0'):
                    list.append(0)
                elif(char == '1'):
                    list.append(1)
                elif(char == '['):
                    depth += 1
                    array = []
                    list.append(array)
                    saveList.append(array)
                elif(char == ']'):
                    depth -= 1
                    saveList.pop()
                else:
                    pass
                char = file.read(1)
        return QuadTree.fromList(list) 

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """Returns a quadtree from a list which contains other list or 0 or 1"""
        paramList = []
        depth = 0
        for d in data:
            if isinstance(d, list):
                subQuadtree = QuadTree.fromList(d)
                paramList.append(subQuadtree)
                depth = max(depth, subQuadtree.depth)
            elif(d == 0):
                paramList.append(False)
            elif(d == 1):
                paramList.append(True)
        quadtree = QuadTree(*paramList)
        quadtree._depth = depth + 1
        return quadtree
    
    @depth.setter
    def depth(self, value: int):
        self._depth = value


class TkQuadTree(QuadTree):
    def paint(self):
        """Opens a window with a visual representation of self (quadtree)"""
        root = Tk()
        root.geometry('600x600')
        TkQuadTree.drawQuadtree(self, root, depth=0)
        root.mainloop()

    @staticmethod
    def drawQuadtree(tree : QuadTree, parent : Frame | Tk, depth : int):
        """Manages cells position"""
        TkQuadTree.assignCell(tree.hg, parent, 0, 0, depth)
        TkQuadTree.assignCell(tree.hd, parent, 0, 1, depth)
        TkQuadTree.assignCell(tree.bd, parent, 1, 0, depth)
        TkQuadTree.assignCell(tree.bg, parent, 1, 1, depth)
    
    @staticmethod
    def assignCell(cell : QuadTree | bool, parent : Frame | Tk, row : int, column : int, depth : int):
        """Manages cells content"""
        cellSize = 300 / (2 ** depth)
        if isinstance(cell, QuadTree):
            frame = Frame(parent)
            frame.config(width=cellSize, height=cellSize)
            frame.grid(row=row, column=column, sticky="nsew")
            TkQuadTree.drawQuadtree(cell, frame, depth + 1)
            depth -= 1
        elif(cell == True):
            frame = Frame(parent)
            frame.config(background="black", width=cellSize, height=cellSize)
            frame.grid(row=row, column=column, sticky="nsew")
        elif(cell == False):
            frame = Frame(parent)
            frame.config(background="white", width=cellSize, height=cellSize)
            frame.grid(row=row, column=column, sticky="nsew")
