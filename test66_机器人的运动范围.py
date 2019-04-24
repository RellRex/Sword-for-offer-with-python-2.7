# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.mat=[]
        self.memory=[]
    
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold<=0:
            return 0
        self.create_mat(rows,cols)
        r,c=0,0
        self.mark(r,c)
        i=1
        while True:
            r_n,c_n=self.move(r,c,rows,cols,threshold)
            if r==r_n and c==c_n:
                if len(self.memory)==0:
                    return i
                else:
                    r,c=self.memory.pop()
            else:
                self.memory.append((r,c))
                self.mark(r_n,c_n)
                r,c=r_n,c_n
                i+=1
            
    def desc(self,i,j,k):
        sum_k=0
        while i // 10 != 0:
            sum_k+=(i%10)
            i=i//10
        sum_k+=i
        while j //10 != 0:
            sum_k+=(j%10)
            j=j//10
        sum_k+=j
        if sum_k>k:
            return False
        else:
            return True
    
    def mark(self,i,j):
        self.mat[i][j]="*"
    
    def create_mat(self,rows,cols):
        for i in range(rows):
            self.mat.append([0]*cols)
        
    def move(self,r,c,rows,cols,k):
        # 向上
        if r!=0 and self.mat[r-1][c]!="*" and self.desc(r-1,c,k):
            return r-1,c
        # 向下
        if r!=(rows-1) and self.mat[r+1][c]!="*" and self.desc(r+1,c,k):
            return r+1,c
        # 向左
        if c!=0 and self.mat[r][c-1]!="*" and self.desc(r,c-1,k):
            return r,c-1
        # 向右
        if c!=(cols-1) and self.mat[r][c+1]!="*" and self.desc(r,c+1,k):
            return r,c+1
        return r,c
    
if __name__=="__main__":
    s=Solution()
    print(s.movingCount(5,10,10))
