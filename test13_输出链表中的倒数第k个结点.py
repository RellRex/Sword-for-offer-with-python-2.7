# -*- coding: utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        k_o=k
        if head is None:
            return head
        cur=head;cur_af=head;count=1
        while cur.next is not None:
            cur=cur.next
            k-=1;count+=1
            if k<=0: cur_af=cur_af.next
        if k_o>count or k_o==0:
            return None
        else:
            return cur_af
            