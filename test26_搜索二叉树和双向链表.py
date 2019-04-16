# -*- coding: utf-8 -*-

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class Solution:
    def __init__(self):
        self.lst=[]
        
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        
        self.mid_tree(pRootOfTree);i=0
        n=len(self.lst)
        while i<(n-1):
            self.lst[i].right=self.lst[i+1]
            i+=1
        self.lst[i].right=None
        
        j=n-1
        while j>0:
            self.lst[j].left=self.lst[j-1]
            j-=1
        self.lst[j].left=None
        return self.lst[0]
            
    def mid_tree(self,root):
        if root is None:
            return 
        self.mid_tree(root.left)
        self.lst.append(root)
        self.mid_tree(root.right)
        