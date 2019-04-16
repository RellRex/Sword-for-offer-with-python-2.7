# -*- coding: utf-8 -*-

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k>len(tinput):
            return []
        if len(tinput)==0:
            return []
        
        result=self.merge_sort(tinput)
        return result[:k]
        
    def merge_sort(self,alist):
        n=len(alist)
        mid=n//2
        if n==1:
            return alist
        
        left_li=self.merge_sort(alist[:mid])
        right_li=self.merge_sort(alist[mid:])
        
        result=[]
        left_pointer,right_pointer=0,0
        while left_pointer<len(left_li) and right_pointer<len(right_li):
            if left_li[left_pointer]<right_li[right_pointer]:
                result.append(left_li[left_pointer])
                left_pointer+=1
            else:
                result.append(right_li[right_pointer])
                right_pointer+=1
            
        result+=left_li[left_pointer:]
        result+=right_li[right_pointer:]
        return result
        
        
if __name__=="__main__":
    s=Solution()
    a=[]
    print(s.GetLeastNumbers_Solution(a,0))