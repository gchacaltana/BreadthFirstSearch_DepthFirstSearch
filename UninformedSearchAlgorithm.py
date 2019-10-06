#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Uninformed Search Algorithm
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

from Node import Node


class UnniformedSearchAlgorithm(object):
    def __init__(self, listNodes, searched):
        self.listNodes = listNodes
        self.searched = searched
        self.createQueue()

    def createQueue(self):
        self.queue = []
        self.queue.append(self.listNodes[0])

    def addQueue(self, node):
        pass

    def readQueue(self):
        return self.queue.pop(0)

    def getQueueLen(self):
        return len(self.queue)

    def getNodeFromList(self, name):
        for node in self.listNodes:
            if node.name == name:
                return node

    def validateLenQueue(self):
        if self.getQueueLen() == 0:
            raise Exception("La cola esta vacia")

    def matchSearched(self, nodeName):
        if nodeName == self.searched:
            raise Exception("Ciudad encontrada: %s" % nodeName)

    def search(self):
        pass

    def insertNodeChildQueue(self, node):
        childrenNodes = node.getChildrenNodes()
        for child in childrenNodes:
            childNode = self.getNodeFromList(child.name)
            if (isinstance(childNode, Node)):
                self.addQueue(childNode)
