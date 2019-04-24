# -*- coding: utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.tree_lst=[]
        
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return self.tree_lst
        lst=[pRoot];i=1
        while lst:
            n=len(lst);tree_sub=[]
            for j in range(n):
                node=lst.pop(0)
                tree_sub.append(node.val)
                if node.left is not None:
                    lst.append(node.left)
                if node.right is not None:
                    lst.append(node.right)
            if i % 2==0:
                self.tree_lst.append(tree_sub[::-1])
            else:
                self.tree_lst.append(tree_sub)
            i+=1
        return self.tree_lst
            
if __name__=="__main__":
    s=Solution()
    