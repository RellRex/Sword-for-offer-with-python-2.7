# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.dict={}
        self.result=[]
        
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        for i in array:
            self.dict[i]=self.dict.get(i,0)+1
        for j,num in self.dict.items():
            if num==1:
                self.result.append(j)
        return self.result
    
if __name__=="__main__":
    s=Solution()
    ss=[2,4,3,6,3,2,5,5]
    print(s.FindNumsAppearOnce(ss))
    