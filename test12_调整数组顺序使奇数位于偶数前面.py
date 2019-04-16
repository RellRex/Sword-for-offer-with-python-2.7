# -*- coding: utf-8 -*-

# 记住前一个奇数的位置，将新的奇数挪到后面
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd=[];even=[]
        for i in range(0,len(array)):
            if array[i]%2==1:
                odd.append(array[i])
            elif array[i]%2==0:
                even.append(array[i])
        return odd+even
        
        
if __name__=="__main__":
    s=Solution()
    lst=[1,2,3,4,5,6,7]
    print(s.reOrderArray(lst))
    