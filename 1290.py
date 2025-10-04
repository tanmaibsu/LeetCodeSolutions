# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        listNode = head
        while listNode:
            print(listNode.val)
            c+=1
            listNode = listNode.next

cls = Solution()
ListNode = ListNode([1, 0, 1])
# ListNode = ListNode(0)
# ListNode = ListNode(1)
cls.getDecimalValue(ListNode)
print(c)