# -*- coding: utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        cur=pHead;lst=[]
        while cur is not None:
            if cur in lst:
                return cur
            lst.append(cur)
            cur=cur.next
        return None
    
if __name__=="__main__":
    s=Solution()
    