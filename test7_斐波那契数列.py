# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.lst=[0,1]
        
    def Fibonacci(self, n):
        # write code here
        m=len(self.lst)-1
        if n<=m:
            return self.lst[n]
        i=2
        while i<=n:
            self.lst.append(self.lst[i-1]+self.lst[i-2])
            i+=1
        return self.lst[i-1]
    
if __name__=="__main__":
    s=Solution()
    print(s.Fibonacci(2))
        