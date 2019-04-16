# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.map={}
        
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        for i in numbers:
            self.map[i]=self.map.get(i,0)+1
        n=len(numbers)/2
        for j in self.map.keys():
            if self.map[j]>n:
                return j
        return 0
        
if __name__=="__main__":
    s=Solution()
    ss=[1,2,3,2,2,2,5,4,2]
    print(s.MoreThanHalfNum_Solution(ss))
    