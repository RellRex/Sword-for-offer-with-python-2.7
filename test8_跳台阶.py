# -*- coding: utf-8 -*-

# 这是一个斐波那契数列
# 这里我们采用递归的形式写斐波那契数列

class Solution:
    def __init__(self):
        self.lst=[1,1]
          
    def jumpFloor(self, number):
        # write code here
        if number==0:
            return self.lst[0]
        item=self.lst[1]
        self.lst[1]=self.lst[0]+self.lst[1]
        self.lst[0]=item
        return self.jumpFloor(number-1)
    
if __name__=="__main__":
    s=Solution()
    print(s.jumpFloor(4))