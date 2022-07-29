# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return head
        
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        middle=slow.next
        slow.next=None
        curr=middle
        prev=None
        
        while curr:
            curr.next,prev,curr=prev,curr,curr.next
            
        head2=prev
        head1=head.next
        curr=head
        
        while head1 and head2:
            curr.next=head2
            head2=head2.next
            curr.next.next=head1
            head1=head1.next
            curr=curr.next.next
            
        curr.next=head1 or head2
            
        return head