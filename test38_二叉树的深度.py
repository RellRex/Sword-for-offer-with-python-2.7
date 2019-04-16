# -*- coding: utf-8 -*-


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        lst=[pRoot];count=0
        while True:
            n=len(lst)
            if n==0:
                return count
            count+=1
            for i in range(n):
                node=lst.pop(0)
                if node.left is not None:
                    lst.append(node.left)
                if node.right is not None:
                    lst.append(node.right)
        
        
if __name__=="__main__":
    s=Solution()
    