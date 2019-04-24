# -*- coding: utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lst=[]
        self.node_lst=[]
        
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None or k<1:
            return None
        self.mid_tree(pRoot)
        if k>len(self.lst):
            return None
        lst_sort=sorted(self.lst)
        num=lst_sort[k-1]
        idx=self.lst.index(num)
        return self.node_lst[idx]
    
    # 中序遍历
    def mid_tree(self,root):
        if root is None:
            return
        self.mid_tree(root.left)
        self.lst.append(root.val)
        self.node_lst.append(root)
        self.mid_tree(root.right)

if __name__=="__main__":
    s=Solution()
    a=[2,8,5,4,3,6,4,3,6]
    print(sorted(a))
    