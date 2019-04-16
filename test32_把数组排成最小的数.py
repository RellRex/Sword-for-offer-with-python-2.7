# -*- coding: utf-8 -*-

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def comp(numbers):
            if len(numbers)==1:
                return numbers
            t1=str(numbers.pop(0))
            t2=str(numbers.pop(0))
            if int(t1+t2)<int(t2+t1):
                numbers.insert(0,int(t1+t2))
            else:
                numbers.insert(0,int(t2+t1))
            return comp(numbers)
        if numbers:
            numbers=sorted(numbers)
            return comp(numbers)[0]
        else:
            return ""
            
if __name__=="__main__":
    s=Solution()
    ss=[1,2,3,4,5]
    print(s.PrintMinNumber(ss))
    