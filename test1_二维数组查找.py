# -*- coding: utf-8 -*-

import numpy as np
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m,n=len(array)-1,len(array[0])-1
        # 不断和最右边的数进行比较，逐渐减少行和列
        i=0;j=n
        while j>=0 and i<=m:
            if target<array[i][j]:
                j-=1
            elif target>array[i][j]:
                i+=1
            elif target==array[i][j]:
                return True
        return False    

if __name__=="__main__":
    my_array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]    
    s=Solution()
    print(s.Find(5,my_array))
    



