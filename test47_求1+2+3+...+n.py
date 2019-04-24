# -*- coding: utf-8 -*-

# 短路求值
# 我们可与发现，如果两个数都是正数，会返回比较大的那个
# 如果其中一个为0，会返回0
# 如果是0和一个负数，也会返回0

class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans=n
        temp=ans and self.Sum_Solution(n-1)
        ans=ans+temp
        return ans
    
if __name__=="__main__":
    s=Solution()
    print(s.Sum_Solution(100))
