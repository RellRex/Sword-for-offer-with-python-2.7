# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def push(self, node):
        # write code here
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        # 这里先有判断是否为空
        if  not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        
if __name__=="__main__":
    s=Solution()
    for i in range(10):
        s.push(i)
    print s.pop()
    print s.pop()