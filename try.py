# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def count(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        count = 1
        cur = head
        while cur and cur.next:
            count += 2
            cur = cur.next.next
        if cur:
            return count
        else:
            return count-1

obj = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(obj.count(head)) # Output: [1,2,4,5]
while head:
    print(head.val, end=" ")
    head = head.next