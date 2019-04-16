# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.dict={}
        
    def FirstNotRepeatingChar(self, s):
        # write code here
        for char in s:
            self.dict[char]=self.dict.get(char,0)+1
        result=[]
        for char,count in self.dict.items():
            if count==1:
                result.append(char)
        if len(result)==0: return -1
        for i in s:
            if i in result:
                return s.index(i)
            
if __name__=="__main__":
    s=Solution()
    ss="hjksajkdgjhasghdjasgp"
    print(s.FirstNotRepeatingChar(ss))
    
    