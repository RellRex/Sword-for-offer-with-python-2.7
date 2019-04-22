# -*- coding: utf-8 -*-

# 斐波那契数列
class Solution:
    def __init__(self):
        self.k=0
        self.lst=[0,1]
        
    def rectCover(self, number):
        # write code here
        if number==0 or number==1:
            return number
        self.feibo(number)
        return self.lst[1]
        
    def feibo(self,number):
        if self.k==number:
            return
        item=self.lst[1]
        self.lst[1]=self.lst[0]+self.lst[1]
        self.lst[0]=item
        self.k+=1
        self.feibo(number)
        
    
if __name__=="__main__":
    s=Solution()
    print(s.rectCover(3))
    