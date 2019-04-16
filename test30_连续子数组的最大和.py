# -*- coding: utf-8 -*-

# 动态规划

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n=len(array)
        dp=[i for i in array]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+array[i],array[i])
        return max(dp)
    
if __name__=="__main__":
    s=Solution()
    ss=[1,-2,3,10,-4,7,2,-5]
    print(s.FindGreatestSumOfSubArray(ss))