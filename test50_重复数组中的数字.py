# -*- coding: utf-8 -*-

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        lst=[]
        for i in numbers:
            if i in lst:
                duplication[0]=i
                return True
            lst.append(i)
        return False
    
if __name__=="__main__":
    s=Solution()
    ss=[2,1,3,1,4]
    print(s.duplicate(ss,[0]))