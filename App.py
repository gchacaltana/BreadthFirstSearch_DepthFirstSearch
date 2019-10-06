#!/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import json
from Node import Node


class App(object):

    def __init__(self):
        self.listNodes = []
        self.parentNode = {}

    def main(self):
        with open("routes.json", "r") as f:
            routes = json.load(f)
        self.createNodes(routes)
        self.displayNodes()

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
        print([n.name for n in self.listNodes])


if __name__ == "__main__":
    app = App()
    app.main()
