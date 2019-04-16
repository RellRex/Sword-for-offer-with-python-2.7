# -*- coding: utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        path=[];lst=[]
        def subFindPath(root):
            if root:
                lst.append(root.val)
                if not root.left and not root.right and sum(lst)==expectNumber:
                    path.append(lst[:])
                else:
                    subFindPath(root.left);subFindPath(root.right)
                lst.pop()
        subFindPath(root)
        return path
    
if __name__=="__main__":
    s=Solution()
    
    