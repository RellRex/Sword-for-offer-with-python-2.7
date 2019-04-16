# -*- coding: utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lst=[]
    
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return self.lst
        lst_node=[root]
        while lst_node:
            node=lst_node.pop(0)
            self.lst.append(node.val)
            if node.left is not None:
                lst_node.append(node.left)
            if node.right is not None:
                lst_node.append(node.right)
        return self.lst
        
if __name__=="__main__":
    s=Solution()
    lst=[None,None]
    print(lst is None)
    