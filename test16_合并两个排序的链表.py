# -*- coding: utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None: return pHead2
        if pHead2 is None: return pHead1
        
        p1=pHead1;p2=pHead2
        if p1.val<p2.val:
            head=p1;p1=p1.next
        else:
            head=p2;p2=p2.next
        
        cur=head
        while p1 is not None and p2 is not None:
            if p1.val<p2.val:
                cur.next=p1;p1=p1.next
            else:
                cur.next=p2;p2=p2.next
            cur=cur.next
        if p1 is None: cur.next=p2
        if p2 is None: cur.next=p1
        return head
        