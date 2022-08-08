# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carry = 0
        tmp = dummy
        
        while l1 or l2 or carry!=0:
            total=0
            if l1!=None:
                total+=l1.val
                l1=l1.next
            if l2!=None:
                total+=l2.val
                l2=l2.next
            total+=carry
            carry=total//10
            new_node=ListNode(total%10)
            tmp.next=new_node
            tmp=tmp.next
            
        return dummy.next