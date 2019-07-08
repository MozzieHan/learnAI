#!/usr/bin/env python
# coding=utf-8

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def append(self, val):
        self.s1.append(val)

    def pop(self):
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        if len(self.s2) == 0:
            raise Exception
        return self.s2.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.append(1)
    queue.append(2)
    queue.append(10)

    print(queue.pop(), " == 1")
    print(queue.pop(), " == 2")
    print(queue.pop(), " == 10")
    print("raise", queue.pop())


