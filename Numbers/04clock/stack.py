# -*- coding:utf-8 -*-
# 栈类


class stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def display(self):
        for i in self.items:
            print(i)

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
