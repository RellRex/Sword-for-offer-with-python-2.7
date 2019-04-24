# -*- coding: utf-8 -*-
# 使用循环链表解决
# 防止除法最大限制
import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self,item):
        self.val=item
        self.next=None
        
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n==0 or m==0:
            return -1
        head=self.build(n)
        return self.omit(head,m)
        
    def omit(self,head,m):
        if head.next==head:
            return head.val
        cur=head;j=0
        while j<(m-2):
            cur=cur.next
            j+=1
        cur.next=cur.next.next
        cur=cur.next
        return self.omit(cur,m)
        
    def build(self,n):
        head=Node(0)
        i=1;cur=head
        while i<n:
            cur.next=Node(i)
            cur=cur.next;i+=1
        cur.next=head
        return head
            
    
if __name__=="__main__":
    s=Solution()
    print(s.LastRemaining_Solution(10,5))
    