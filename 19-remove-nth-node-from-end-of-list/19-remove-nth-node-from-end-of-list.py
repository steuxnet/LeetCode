# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def recursive(node: ListNode) -> int:
            depth = -1 if node == None else recursive(node.next)
            if depth == n:
                node.next = None if node.next is None else node.next.next
            return depth + 1 
        return head.next if recursive(head) == n else head