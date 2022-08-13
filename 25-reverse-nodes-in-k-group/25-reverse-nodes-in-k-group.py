# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
            
        return count
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=self.count(head)
        stack=[]
        start=head
        end=head
        original_k=k
        
        while end:
            while k!=0 and end!=None:
                stack.append(end.val)
                end=end.next
                k-=1
            if(n%original_k!=0):
                if end==None:
                    break
            while start!=end:
                start.val=stack.pop()
                start=start.next
                
            k=original_k
        return head