# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = temp = ListNode()
        arr = []
        while head:
            if head.val not in nums:
                arr.append(head.val)
            head = head.next
        for i in arr:
            temp.next= ListNode(i)
            temp = temp.next
        return head2.next