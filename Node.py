#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Node Class
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

class Node(object):
    def __init__(self, name):
        self.childNodes = []
        self.name = name

    def addChild(self,node):
        self.childNodes.append(node)

    def getChildrenNodes(self):
        return [child.name for child in self.childNodes]
