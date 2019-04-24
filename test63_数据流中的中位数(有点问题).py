# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.lst=[]
        
    def Insert(self, num):
        # write code here
        self.lst.append(num)
    
    def GetMedian(self):
        # write code here
        sorted_lst=sorted(self.lst)
        n=len(self.lst)
        if n%2==1:
            return sorted_lst[n//2]
        else:
            return float(sorted_lst[n//2]+sorted_lst[(n//2)-1])/2
    
    
if __name__=="__main__":
    s=Solution()
    s.Insert(0)
    s.Insert(1)
    s.Insert(2)
    s.Insert(3)
    print(s.GetMedian())
    