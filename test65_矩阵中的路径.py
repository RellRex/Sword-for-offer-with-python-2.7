# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.lst=[]   # 记录初始的位置
        self.mat=[]   # 矩阵地图
        self.memory=[]  # 记录回溯的点
        
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.first_char(matrix,path[0])
        while self.lst:
            self.create_map(matrix,rows,cols)
            beg=self.lst.pop(0)
            r,c=beg // cols,beg % cols
            self.mark(r,c)
            n=len(path);i=1
            while i<n:
                r_n,c_n=self.search(r,c,path[i],rows,cols)
                self.mark(r_n,c_n)
                if r==r_n and c==c_n:
                    if len(self.memory)==0: 
                        break
                    else:
                        r,c=self.memory.pop()
                        i-=1
                else:
                    self.memory.append((r,c))
                    r,c=r_n,c_n
                    i+=1
            if i==n:
                return True
        return False
    
    def create_map(self,matrix,rows,cols):
        """构造矩阵"""
        self.mat=[]
        for j in range(rows):
            lst_mat=[]
            for i in range(cols):
                lst_mat.append(matrix[j*cols+i])
            self.mat.append(lst_mat)
    
    def first_char(self,mat,char):
        """寻找可能的初始位置"""
        n=len(mat)
        for i in range(n):
            if mat[i]==char:
                self.lst.append(i)
                
    def mark(self,i,j):
        """对走过的点进行标记"""
        self.mat[i][j]="*"
        
    def search(self,r,c,i,rows,cols):
        """对上下左右进行搜索"""
        # 向上
        if r!=0 and self.mat[r-1][c]==i:
            return r-1,c
        # 向下
        if r!=rows-1 and self.mat[r+1][c]==i:
            return r+1,c
        # 向左
        if c!=0 and self.mat[r][c-1]==i:
            return r,c-1
        #  向右
        if c!=cols-1 and self.mat[r][c+1]==i:
            return r,c+1
        else:
            return r,c
            
        
if __name__=="__main__":
    s=Solution()
    mat="ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
    rows=5;cols=8
    path="SGGFIECVAASABCEHJIGQEM"
    print(s.hasPath(mat,rows,cols,path))