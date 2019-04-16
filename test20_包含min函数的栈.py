# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.stack=[]
        self.assist=[]
        
    def push(self, node):
        # write code here
        self.stack.append(node)
        min_d=self.min()
        if not min_d or min_d>node:
            self.assist.append(node)
        else:
            self.assist.append(min_d)
        
    def pop(self):
        # write code here
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
        
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        
    def min(self):
        # write code here
        if self.assist:
            return self.assist[-1]