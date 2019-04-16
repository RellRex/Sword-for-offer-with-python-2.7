# -*- coding: utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        elif pHead.next is None:
            return pHead
        elif pHead.next.next is None:
            now=pHead
            pre=pHead.next
            now.next=None
            pre.next=now
            return pre
        
        pre=pHead.next
        cur=pre.next
        now=pHead
        pHead.next=None
        while cur is not None:
            pre.next=now
            now=pre
            pre=cur
            cur=cur.next
        pre.next=now
        return pre
    