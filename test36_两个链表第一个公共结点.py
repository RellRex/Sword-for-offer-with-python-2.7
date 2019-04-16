# -*- coding: utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        cur1=pHead1;node=[]
        while cur1 is not None:
            node.append(cur1)
            cur1=cur1.next
        cur2=pHead2
        while cur2 is not None:
            if cur2 in node:
                return cur2
            cur2=cur2.next
        return False
    
if __name__=="__main__":
    s=Solution()
    