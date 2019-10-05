#!/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script

__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from Node import Node

class App(object):
    nodes = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initNodes()

    def initNodes(self):
        self.nodes = ["Tumbes", "Trujillo", "Moyobamba", "Iquitos"]
        node1 = Node("Tumbes")
        node2 = Node("Trujilo")
        node3 = Node("Iquitos")
        node4 = Node("Moyobamba")
        node1.addChild(node2)
        node1.addChild(node3)
        node1.addChild(node4)

    def displayNodes(self):
        print([n for n in self.nodes])

if __name__ == "__main__":
    app = App()
    app.displayNodes()