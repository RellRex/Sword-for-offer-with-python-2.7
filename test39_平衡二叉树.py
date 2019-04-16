# -*- coding: utf-8 -*-

# 平衡二叉树：一棵空树或者左右两个子树的高度差的绝对值不超过1
# 统计左右两棵子树的深度，进行比较

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return self.panduan(pRoot)
        
    def panduan(self,pRoot):
        count_left=self.tree_depth(pRoot.left)
        count_right=self.tree_depth(pRoot.right)
        if abs(count_left-count_right)>1:
            return False
        
        if pRoot.left is not None:
            left=self.panduan(pRoot.left)
        else:left=True
        
        if pRoot.right is not None:
            right=self.panduan(pRoot.right)
        else:right=True
        
        # 左子树或者右子树不平衡，返回不平衡
        if left==False or right==False:
            return False
        
        return True
        
    def tree_depth(self,root):
        if root is None:
            return 0
        lst=[root];count=0
        while lst:
            n=len(lst);count+=1
            for i in range(n):
                node=lst.pop(0)
                if node.left is not None:
                    lst.append(node.left)
                if node.right is not None:
                    lst.append(node.right)
        return count
    
if __name__=="__main__":
    s=Solution()
    