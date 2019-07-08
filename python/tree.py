#!/usr/bin/env python
# coding=utf-8
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            nodes = [self.root]
            while nodes:
                node = nodes.pop(0)
                if node.left is None:
                    node.left = Node(val)
                    return
                if node.right is None:
                    node.right = Node(val)
                    return
                nodes.append(node.left)
                nodes.append(node.right)

    def pre(self, node):
        if node is None:
            return
        print(node.val)
        self.pre(node.left)
        self.pre(node.right)
    def mid(self, node):
        if node is None:
            return
        self.mid(node.left)
        print(node.val)
        self.mid(node.right)
    def fin(self, node):
        if node is None:
            return
        self.fin(node.left)
        self.fin(node.right)
        print(node.val)

    def p(self):
        nodes = [self.root]
        while len(nodes) != 0:
            node = nodes.pop(0)
            if node.left != None:
                nodes.append(node.left)
            if node.right != None:
                nodes.append(node.right)
            print(node.val)


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(11)
    tree.root.left.right = Node(12)
    tree.root.right.left = Node(13)
    tree.root.right.right = Node(14)
    tree.root.left.left.left = Node(111)

    tr = Tree()
    tr.add(1)
    tr.add(2)
    tr.add(3)
    tr.add(4)
    tr.add(5)
    tr.add(6)
    tr.add(7)
    tr.add(11)
    tr.add(13)
    tr.add(15)

    tr.p()
    print("=================")
    tr.pre(tr.root)
