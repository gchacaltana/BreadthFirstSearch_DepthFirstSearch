#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from Node import Node


class BFS(object):
    def __init__(self, firstNode, searched):
        self.queue = []
        self.addQueue(firstNode)
        self.searched = searched

    def addQueue(self, node):
        self.queue.append(node)

    def readQueue(self):
        return self.queue.pop(0)

    def getQueueLen(self):
        return len(self.queue)

    def search(self):
        nodeName = None
        count = 0
        while(True):
            count += 1
            print("elementos queue: ", self.getQueueLen())
            if self.getQueueLen() > 0:
                node = self.readQueue()
                print("Leyendo %s" % (node.name))
                if node.name == self.searched:
                    break
                else:
                    childrenNodes = node.getChildrenNodes()
                    for child in childrenNodes:
                        self.addQueue(child)
                    print([n.name for n in self.queue])
            else:
                print("La cola se quedo sin elementos")
                break
            if count == 20:
                break
