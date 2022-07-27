# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        
        tmp=head
        length=0
        while tmp:
            tmp=tmp.next
            length+=1
            
        if n==length:
            return head.next
        
        count=length-n-1
        
        tmp=head
        while count!=0:
            tmp=tmp.next
            count-=1
            
        tmp.next=tmp.next.next
        return head