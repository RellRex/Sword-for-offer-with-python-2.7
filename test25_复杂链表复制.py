# -*- coding: utf-8 -*-

# 思路：
# 1.在旧的链表中创建新的链表
# 2.根据旧的链表，初始化新的链表
# 3.拆分新的链表

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        if pHead.next is None:
            return RandomListNode(pHead.label)
        
        # 在旧表中复制新表
        cur=pHead;nxt=pHead.next
        while nxt is not None:
            node=RandomListNode(cur.label)
            cur.next=node;node.next=nxt
            cur=nxt;nxt=nxt.next
        node=RandomListNode(cur.label)
        cur.next=node;node.next=None
        
        # 进行random指针的连接
        cur=pHead
        while cur is not None:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        
        # 把新表拆出
        cur=pHead.next;nxt=cur.next.next
        pHead.next=None;head=cur
        while nxt.next is not None:
            cur.next=nxt
            cur=nxt;nxt=nxt.next.next
        cur.next=nxt
        return head
        
        
        
        
        
        
            