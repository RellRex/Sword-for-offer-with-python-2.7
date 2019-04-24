# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.dict={}
        self.lst=[]
        
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for i in self.lst:
            if self.dict[i]==1:
                return i
        return "#"
        
    def Insert(self, char):
        # write code here
        self.dict[char]=self.dict.get(char,0)+1
        self.lst.append(char)
        
if __name__=="__main__":
    s=Solution()
    s.Insert(0)
    s.Insert(1)
    s.Insert(2)
    print(s.FirstAppearingOnce())
    