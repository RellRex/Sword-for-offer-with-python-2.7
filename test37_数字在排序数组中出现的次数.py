# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.dict={}
        
    def GetNumberOfK(self, data, k):
        # write code here
        for i in data:
            self.dict[i]=self.dict.get(i,0)+1
        return self.dict.get(k,0)

if __name__=="__main__":
    s=Solution()
    data=[1,2,3,3,3,3,4,5];n=3
    print(s.GetNumberOfK(data,n))
    