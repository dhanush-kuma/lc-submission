# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=""
        n2=""
        while l1!=None:
              n1=str(l1.val)+n1
              l1=l1.next
              
        while l2!=None:
            n2=str(l2.val)+n2
            l2=l2.next
        n=int(n1)+int(n2)
        n=str(n)
        f=1
        for c in n:
            if f==1:
                node=ListNode(c,None)
                f=0
            else:
                newnode=ListNode(c,node)
                node=newnode
        return node