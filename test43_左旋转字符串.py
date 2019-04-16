# -*- coding: utf-8 -*-

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        m=len(s)
        if n==0 or m==0 or m<=n:return s
        return s[n:]+s[:n]
    
if __name__=="__main__":
    s=Solution()
    ss="XYZdefabc"
    print(s.LeftRotateString(ss,9))
    