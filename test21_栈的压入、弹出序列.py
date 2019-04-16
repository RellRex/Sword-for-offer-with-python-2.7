# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        self.stack=[]
    
    def push(self,node):
        self.stack.append(node)
            
    def pop(self):
        if self.stack:
            return self.stack.pop()
    
    def IsPopOrder(self, pushV, popV):
        # write code here
        m,n=len(pushV),len(popV)
        j=0
        for i in range(m):
            if pushV[i] != popV[j]:
                self.push(pushV[i])
            else:
                j+=1
        while j<n:
            if self.pop() != popV[j]:
                return False
            j+=1
        return True
    
if __name__=="__main__":
    s=Solution()
    pushV=[1,2,3,4,5];popV=[4,5,3,2,1]
    print(s.IsPopOrder(pushV,popV))
    
