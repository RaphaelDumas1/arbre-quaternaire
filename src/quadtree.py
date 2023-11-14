from __future__ import annotations
from tkinter import *
from tkinter import ttk

class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return 1

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """"For entertaining :D"""
        depthList = []
        depth = 0
        list = None
        with open(filename, 'r') as file:
            char = file.read(1)
            while char:
                if(len(depthList) != 0):
                    list = depthList[depth - 1]    
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
                    depthList.append(array)
                elif(char == ']'):
                    depth -= 1
                    depthList.pop()
                else:
                    pass
                char = file.read(1)
        return QuadTree.fromList(list) 

    @staticmethod
    def fromList(data: list):
        test = []
        for i, d in enumerate(data):
            if isinstance(d, list):
                test.append(QuadTree.fromList(d))
            elif(d == 0):
                test.append(False)
            elif(d == 1):
                test.append(True)
        return QuadTree(*test)


    @property
    def hg(self) -> bool | "QuadTree":
        return self._hg

    @hg.setter
    def hg(self, value: bool | "QuadTree") -> None:
        self._hg = value

    @property
    def hd(self) -> bool | "QuadTree":
        return self._hd

    @hd.setter
    def hd(self, value: bool | "QuadTree") -> None:
        self._hd = value

    @property
    def bd(self) -> bool | "QuadTree":
        return self._bd

    @bd.setter
    def bd(self, value: bool | "QuadTree") -> None:
        self._bd = value

    @property
    def bg(self) -> bool | "QuadTree":
        return self._bg

    @bg.setter
    def bg(self, value: bool | "QuadTree") -> None:
        self._bg = value

class TkQuadTree(QuadTree):
    def paint(self):
        root = Tk()
        root.geometry('600x600')
        TkQuadTree.iterateTree(self, root, depth=0)
        root.mainloop()

    @staticmethod
    def iterateTree(tree : QuadTree, parent, depth):
        TkQuadTree.methodeTest(tree.hg, parent, 0, 0, depth)
        TkQuadTree.methodeTest(tree.hd, parent, 0, 1, depth)
        TkQuadTree.methodeTest(tree.bg, parent, 1, 0, depth)
        TkQuadTree.methodeTest(tree.bd, parent, 1, 1, depth)
    
    @staticmethod
    def methodeTest(tree : QuadTree | bool, parent, row, column, depth):
        cell_size = 200 / (2 ** depth)
        if isinstance(tree, QuadTree):
            frame = Frame(parent)
            frame.config(width=cell_size, height=cell_size)
            frame.grid(row=row, column=column)
            TkQuadTree.iterateTree(tree, frame, depth + 1)
            depth -= 1
        elif(tree == True):
            frame = Frame(parent)
            frame.config(background="black", width=cell_size, height=cell_size)
            frame.grid(row=row, column=column)
        elif(tree == False):
            frame = Frame(parent)
            frame.config(background="white", width=cell_size, height=cell_size)
            frame.grid(row=row, column=column)
