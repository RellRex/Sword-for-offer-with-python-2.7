# -*- coding: utf-8 -*-

# 对称：如果一棵二叉树和这棵二叉树的镜像是同样的，定义其为对称的

# 求一颗树的镜像
# 对比两棵树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        root=TreeNode(pRoot.val)
        self.mirror(pRoot,root)
        return self.same_tree(pRoot,root)
        
    def mirror(self,pRoot,root):
        if pRoot is None:
            return
        if pRoot.left is not None:
            root.right=TreeNode(pRoot.left.val)
        if pRoot.right is not None:
            root.left=TreeNode(pRoot.right.val)
        
        self.mirror(pRoot.left,root.right)
        self.mirror(pRoot.right,root.left)
    
    def same_tree(self,pRoot,pRootm):
        if pRoot is None and pRootm is None:
            return True
        elif pRoot is None:
            return False
        elif pRootm is None:
            return False
        if pRoot.val != pRootm.val:
            return False
        
        left=self.same_tree(pRoot.left,pRootm.left)
        right=self.same_tree(pRoot.right,pRootm.right)
        
        if left and right:
            return True
        else:
            return False
        
if __name__=="__main__":
    s=Solution()
