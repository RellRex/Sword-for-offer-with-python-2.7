# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def __init__(self):
        self.dist={}
        
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return None
        
        cur=pHead
        while cur is not None:
            self.dist[cur.val]=self.dist.get(cur.val,0)+1
            cur=cur.next
            
        while pHead is not None and self.dist[pHead.val]>1:
            pHead=pHead.next
        if pHead is None:
            return None
        
        pre=pHead;cur=pre.next
        while cur is not None:
            if self.dist[cur.val]>1:
                pre.next=cur.next
            else:
                pre=pre.next
            cur=cur.next
        return pHead
        
if __name__=="__main__":
    s=Solution()
    lst=[2,3,3,4,4,5]
    pHead=ListNode(1);cur=pHead
    for i in lst:
        node=ListNode(i)
        cur.next=node
        cur=cur.next
    head=s.deleteDuplication(pHead)
    curf=head
    while curf is not None:
        print(curf.val)
        curf=curf.next