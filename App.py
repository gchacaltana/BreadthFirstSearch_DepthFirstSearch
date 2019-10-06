#!/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import json
from Node import Node
from BFS import BFS

class App(object):

    def __init__(self):
        self.listNodes = []
        self.parentNode = {}

    def main(self, jsonfile):
        with open(jsonfile, "r") as f:
            routes = json.load(f)
        self.createNodes(routes)
        self.displayNodes()
        self.breadthFirstSearch()

    def createNodes(self, routes):
        i = 0
        for n in routes:
            i += 1
            self.parentNode[i] = Node(n)
            for cn in routes[n]:
                childNode = Node(cn)
                self.parentNode[i].addChild(childNode)
            self.listNodes.append(self.parentNode[i])

    def displayNodes(self):
        print("Lista de Nodos")
        print([n.name for n in self.listNodes])

    def breadthFirstSearch(self):
        print("Busqueda Breadth First Search")
        bsf = BFS(self.listNodes[0], "Arequipa")
        bsf.search()

if __name__ == "__main__":
    app = App()
    app.main("routes.json")
