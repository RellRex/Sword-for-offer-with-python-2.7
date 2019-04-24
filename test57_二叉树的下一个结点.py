# -*- coding: utf-8 -*-

# 我的方法是首先去寻找了树的根结点
# 进行中序遍历，然后输出结果

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def __init__(self):
        self.lst=[]
        
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        
        root=pNode
        while root.next is not None:
            root=root.next
            
        self.mid_tree(root)
        idx=self.lst.index(pNode)
        if idx+1 >= len(self.lst):
            return None
        else:
            return self.lst[idx+1]
    
    def mid_tree(self,root):
        if root is None:
            return
        self.mid_tree(root.left)
        self.lst.append(root)
        self.mid_tree(root.right)
        
if __name__=="__main__":
    s=Solution()
    