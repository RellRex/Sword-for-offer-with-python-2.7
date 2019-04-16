# -*- coding: utf-8 -*-

# 我们可以使用sorted函数
"""
def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        a=sorted(tinput)
        if k>len(a):
            return []
        return a[:k]
"""

# 下面我们回顾一些排序方法
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        self.quick_sort(tinput,0,len(tinput)-1)
        return tinput[:k]
        
    def quick_sort(self,alist,begin,end):
        if begin>=end:
            return
        
        value=alist[begin]
        low=begin;high=end
        while low<high:
            while high>low and alist[high]>=value:
                high-=1
            alist[low]=alist[high]
            while high>low and alist[low]<=value:
                low+=1
            alist[high]=alist[low]
        alist[low]=value
        
        self.quick_sort(alist,begin,low-1)
        self.quick_sort(alist,low+1,end)
        
        
if __name__=="__main__":
    s=Solution()
    a=[4,5,1,6,2,7,3,8]
    print(s.GetLeastNumbers_Solution(a,4))