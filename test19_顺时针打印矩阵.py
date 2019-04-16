# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.lst=[]
        
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        n,m=len(matrix)-1,len(matrix[0])-1
        if n==1:
            self.lst.extend(matrix[0])
            self.lst.extend(matrix[n][::-1])
            return
        elif n==0:
            self.lst.extend(matrix[0])
            return 
            
        self.lst.extend(matrix[0])
        for i in range(1,n):
            self.lst.append(matrix[i][m])
        self.lst.extend(matrix[n][::-1])
        for i in range(n-1,0,-1):
            self.lst.append(matrix[i][0])
        
        matrix_new=[]
        for i in range(1,n):
            matrix_new.append(matrix[i][1:m])
        
        self.printMatrix(matrix_new)
        
if __name__=="__main__":
    s=Solution()
    lst=[[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
    # lst=[[1]]
    s.printMatrix(lst)
    print(s.lst)        
        