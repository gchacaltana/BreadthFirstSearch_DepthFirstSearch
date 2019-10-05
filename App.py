#!/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script

__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from Node import Node

class App(object):
    listNodes = []
    parentNode = {}
    def __init__(self, nodes):
        self.nodes = nodes
        self.createNodes()

    def createNodes(self):
        i = 0
        for n in self.nodes:
            i +=1
            self.parentNode[i] = Node(n)
            #print(i)
            #print([c for c in self.nodes[n]])
            #print("-----------")
            for cn in self.nodes[n]:
                childNode = None
                childNode = Node(cn)
                self.parentNode[i].addChild(childNode)
                if cn not in [node.name for node in self.listNodes]:
                    self.listNodes.append(childNode)
            if n not in [node.name for node in self.listNodes]:
                self.listNodes.append(self.parentNode[i])

    def displayNodes(self):
        print([n.name for n in self.listNodes])

if __name__ == "__main__":
    nodes = {}
    nodes["Tumbes"] = ["Trujillo", "Moyobamba", "Iquitos"]
    nodes["Trujillo"] = ["Lima", "Huancayo"]
    nodes["Lima"] = ["Ica", "Ayacucho"]
    nodes["Ica"] = ["Arequipa"]
    nodes["Arequipa"] = ["Moquegua"]
    nodes["Moyobamba"] = ["Huancayo"]
    nodes["Huancayo"] = ["Ayacucho", "Cusco"]
    nodes["Ayacucho"] = ["Abancay", "Ica"]
    nodes["Cusco"] = ["Puno", "Arequipa"]
    nodes["Puno"] = ["Moquegua"]
    nodes["Moquegua"] = ["Tacna"]
    nodes["Iquitos"] = ["Pucallpa"]
    nodes["Pucallpa"] = ["Huancayo"]
    app = App(nodes)
    #app.displayNodes()
    for i in app.parentNode:
        print("Nodo Padre: ", app.parentNode[i].name)
        print("Nodos Hijos: ", app.parentNode[i].getChildrenNodes())
    