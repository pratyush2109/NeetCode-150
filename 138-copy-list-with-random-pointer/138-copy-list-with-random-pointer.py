"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        if head.next==None:
            new_head=Node(head.val)
            new_head.next=None
            if head.random:
                new_head.random=new_head
            else:
                new_head.random=None
            return new_head
        
        curr=head
        nex=head.next
        
        while nex:
            new=Node(curr.val)
            new.next=nex
            curr.next=new
            
            curr=nex
            nex=nex.next
            
        new=Node(curr.val)
        curr.next=new
        
        prev=head
        curr=head.next
        
        while prev and curr and prev.next and curr.next:
            if prev.random:
                curr.random=prev.random.next
            else:
                curr.random=None
            prev=prev.next.next
            curr=curr.next.next
            
        if prev.random:
            curr.random=prev.random.next
        else:
            curr.random=None
            
        new_head=head.next
        curr=new_head
        while curr.next:
            curr.next=curr.next.next
            curr=curr.next
            
        return new_head