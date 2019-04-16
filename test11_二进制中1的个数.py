# -*- coding: utf-8 -*-

class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count

        
if __name__=="__main__":
    s=Solution()
    print(s.NumberOf1(-1))
    