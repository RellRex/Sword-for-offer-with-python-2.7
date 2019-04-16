# -*- coding: utf-8 -*-

class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s)==0: return s
        lst=s.split(" ")
        return " ".join(lst[::-1])
    
if __name__=="__main__":
    s=Solution()
    ss="student. a am I"
    print(s.ReverseSentence(ss))