# -*- coding: utf-8 -*-

# python默认的最大递归深度为998
# 这里我们可以自定义最大递归深度
import sys
sys.setrecursionlimit(30000)

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        def sub_count(f,i):
            if i>n:
                return f
            count=self.count_1(i)
            f+=count
            return sub_count(f,i+1)
        i=1;f=0
        return sub_count(f,i)
            
    def count_1(self,a):
        count=0
        while a>0:
            if a % 10==1:
                count+=1
            a=a//10
        if a==1: count+=1
        return count
    
if __name__=="__main__":
    s=Solution()
    print(s.NumberOf1Between1AndN_Solution(10000))