# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def __init__(self):
        self.root=None
    
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        self.root=TreeNode(pre[0])
        self.tree(self.root,pre,tin)
        return self.root
        
    def tree_split(self,pre,tin):
        """切分"""
        rt=tin.index(pre[0])
        tin_left=tin[0:rt];tin_right=tin[rt+1:]
        m=len(tin_left)
        pre_left=pre[1:(1+m)];pre_right=pre[(m+1):]
        return pre_left,pre_right,tin_left,tin_right
    
    def tree(self,root,pre,tin):
        pre_left,pre_right,tin_left,tin_right=self.tree_split(pre,tin)
        if len(pre_left)>0:
            root.left=TreeNode(pre_left[0])
            self.tree(root.left,pre_left,tin_left)
        if len(pre_right)>0:
            root.right=TreeNode(pre_right[0])
            self.tree(root.right,pre_right,tin_right)
            
                 
if __name__=="__main__":
    s=Solution()
    pre=[1,2,3,4,5,6,7]
    tin=[3,2,4,1,6,5,7]
    root=s.reConstructBinaryTree(pre,tin)
    print(s.root.right.val)
    print(set([1,2,3]))
    