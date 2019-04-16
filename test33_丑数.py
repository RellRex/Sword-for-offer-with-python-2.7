# -*- coding: utf-8 -*-

# 后面的丑数都是前面乘2,3,5得来的

class Solution:
    def __init__(self):
        self.lst=[1]
        self.basic=[2,3,5]
        
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index==1:
            return 1
        if index==0:
            return 0
        i=0;count=1
        while True:
            for j in self.basic:
                num=self.lst[i]*j
                if num not in self.lst: 
                    self.lst.append(num)
                    count+=1
            self.lst=sorted(self.lst);i+=1
            if count > index+100:
                return self.lst[index-1]
    
if __name__=="__main__":
    s=Solution()
    # 1,2,3,4,5,6,8,9,10,12,15,16,18,20,24,25
    print(s.GetUglyNumber_Solution(1500))

