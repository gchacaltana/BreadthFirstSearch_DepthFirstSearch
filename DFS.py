#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Depth First Search Algorithm
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from Node import Node
from UninformedSearchAlgorithm import UnniformedSearchAlgorithm


class DFS(UnniformedSearchAlgorithm):

    def __init__(self, listNodes, searched):
        UnniformedSearchAlgorithm.__init__(self, listNodes, searched)

    def addQueue(self, node):
        if node.name not in [n.name for n in self.queue]:
            self.queue.insert(0, node)

    def search(self):
        try:
            nodeName = None
            count = 0
            while(True):
                self.validateLenQueue()
                count += 1
                print("\nIteracion: ", count)
                node = self.readQueue()
                print("Leyendo %s" % (node.name))
                self.matchSearched(node.name)
                self.insertNodeChildQueue(node)
                print("Queue: ", [n.name for n in self.queue])
        except (Exception) as error:
            print(error)
