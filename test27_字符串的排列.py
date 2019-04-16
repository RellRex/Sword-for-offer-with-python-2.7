# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        self.all=[]
        self.len=0
        
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        
        self.len=len(ss)
        lst=sorted(ss)
        a=[0]*len(ss)
        self.pailie(a,lst)
        result=[]
        for i in self.all:
            if i not in result:
                result.append(i)
        return sorted(result)
        
    def pailie(self,a,lst):
        if len(lst)==0:
            self.all.append("".join(a))
            return
        for i in range(len(lst)):
            j=self.len-len(lst)
            a[j]=lst[i]
            self.pailie(a,lst[:i]+lst[i+1:])
            
if __name__=="__main__":
    s=Solution()
    a=""
    result=s.Permutation(a)
    print(result)