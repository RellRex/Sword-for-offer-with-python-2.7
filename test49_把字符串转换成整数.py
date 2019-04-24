# -*- coding: utf-8 -*-

class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s)==0:
            return 0
        numlst=["0","1","2","3","4","5","6","7","8","9"]
        label=1;sum_num=0
        if s[0]=="+":
            label=1
        elif s[0]=="-":
            label=-1
        elif s[0] in numlst:
            sum_num+=int(s[0])
        else:
            return 0
        
        for string in s[1:]:
            if string in numlst:
                sum_num=sum_num*10+int(string)
            else:
                return 0
        return label*sum_num
    
if __name__=="__main__":
    s=Solution()
    ss="123"
    print(s.StrToInt(ss))
    