# -*- coding: utf-8 -*-

# 因为是递增的序列
# 所以我们可以首先确定一个数，然后用二分查找另一个数是否存在
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        lst=[];len_arr=len(array)
        for i in range(len_arr):
            x=tsum-array[i]
            if self.find(array[i+1:],x):
                lst.append([array[i],x])
        n=len(lst)
        if n==0:
            return []
        elif n==1:
            return lst[0]
        else:
            return self.mulp_min(lst)
            
    def find(self,array,x):
        n=len(array)
        if n==0: return False
        mid=n/2
        if array[mid]==x: return True
        elif  array[mid]<x: 
            return self.find(array[mid+1:],x)
        elif array[mid]>x: 
            return self.find(array[:mid],x)
        
    def mulp_min(self,lst):
        min_mulp=10000;min_num=0
        for num in lst:
            x=num[0]*num[1]
            if x<min_mulp:
                min_mulp=x
                min_num=num
        return min_num               
    
if __name__=="__main__":
    s=Solution()
    a=[1,2,4,7,11,15]
    print(s.FindNumbersWithSum(a,15))
    