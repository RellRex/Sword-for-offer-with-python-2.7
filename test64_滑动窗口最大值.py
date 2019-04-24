# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.lst=[]
        self.win_lst=[]
        
    def maxInWindows(self, num, size):
        # write code here
        n=len(num)
        if n==0 or size==0 or size>n:
            return []
        self.lst.extend(num[:size])
        self.win_lst.append(max(self.lst))
        for i in range(size,n):
            self.lst.pop(0)
            self.lst.append(num[i])
            self.win_lst.append(max(self.lst))
        return self.win_lst
    
if __name__=="__main__":
    s=Solution()
    num=[2,3,4,2,6,2,5,1];size=3
    print(s.maxInWindows(num,size))