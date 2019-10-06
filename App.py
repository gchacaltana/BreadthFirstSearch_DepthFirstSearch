#!/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import json
from Node import Node
from BFS import BFS
from DFS import DFS

class App(object):

    def __init__(self, jsonfile, searched):
        self.listNodes = []
        self.parentNode = {}
        self.jsonfile = jsonfile
        self.searched = searched

    def main(self):
        self.openFile()
        self.createNodes()
        self.displayNodes()
        self.breadthFirstSearch()
        self.depthFirstSearch()

    def openFile(self):
        print("\n1. Abriendo fichero")
        with open(self.jsonfile, "r") as f:
            self.routes = json.load(f)

    def createNodes(self):
        i = 0
        print("\n2. Cargando nodos")
        for n in self.routes:
            i += 1
            self.parentNode[i] = Node(n)
            for cn in self.routes[n]:
                childNode = Node(cn)
                self.parentNode[i].addChild(childNode)
            self.listNodes.append(self.parentNode[i])

    def displayNodes(self):
        print("\n3. Nodos cargados")
        print([n.name for n in self.listNodes])

    def breadthFirstSearch(self):
        print("\nIniciando Busqueda Breadth First Search")
        print("------------------------------------------")
        bsf = BFS(self.listNodes, self.searched)
        bsf.search()
    
    def depthFirstSearch(self):
        print("\nIniciando Busqueda Depth First Search")
        print("------------------------------------------")
        dfs = DFS(self.listNodes, self.searched)
        dfs.search()

if __name__ == "__main__":
    try:
        app = App("routes.json", "Arequipa")
        app.main()
    except (ValueError, FileNotFoundError, AttributeError) as ex:
        print(ex)
