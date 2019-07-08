#!/usr/bin/env python
# coding=utf-8
class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def append(self, val):
        empty_q, other_q = self.find_empty_q()
        empty_q.append(val)
        while len(other_q)>0:
            empty_q.append(other_q.pop(0))

    def pop(self):
        _, other_q = self.find_empty_q()
        if len(other_q) == 0:
            raise 
        return other_q.pop(0)

    def find_empty_q(self):
        if len(self.q1) == 0:
            return self.q1, self.q2
        return self.q2, self.q1



if __name__ == "__main__":
    stack = Stack()
    stack.append(2)
    stack.append(4)
    stack.append(3)

    print(stack.pop(), " == 3")
    print(stack.pop(), " == 4")
    print(stack.pop(), " == 2")
    print(stack.pop(), " raise")

