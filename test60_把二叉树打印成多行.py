# -*- coding: utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.lst=[]
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return self.lst
        node_lst=[pRoot]
        while node_lst:
            n=len(node_lst)
            tree_sub=[]
            for i in range(n):
                node=node_lst.pop(0)
                tree_sub.append(node.val)
                if node.left is not None:
                    node_lst.append(node.left)
                if node.right is not None:
                    node_lst.append(node.right)
            self.lst.append(tree_sub)
        return self.lst
    
if __name__=="__main__":
    s=Solution()
    