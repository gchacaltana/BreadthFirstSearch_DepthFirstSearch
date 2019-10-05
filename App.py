#!/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script

__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from Node import Node

class App(object):
    nodes = {}
    def __init__(self):
        self.initNodes()

    def initNodes(self):
        self.nodes["Tumbes"] = ["Trujillo", "Moyobamba", "Iquitos"]
        self.nodes["Trujillo"] = ["Lima", "Huancayo"]
        self.nodes["Lima"] = ["Ica", "Ayacucho"]
        self.nodes["Ica"] = ["Arequipa"]
        self.nodes["Arequipa"] = ["Moquegua"]
        self.nodes["Moyobamba"] = ["Huancayo"]
        self.nodes["Huancayo"] = ["Ayacucho", "Cusco"]
        self.nodes["Ayacucho"] = ["Abancay", "Ica"]
        self.nodes["Cusco"] = ["Puno", "Arequipa"]
        self.nodes["Puno"] = ["Moquegua"]
        self.nodes["Moquegua"] = ["Tacna"]
        self.nodes["Iquitos"] = ["Pucallpa"]
        self.nodes["Pucallpa"] = ["Huancayo"]
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