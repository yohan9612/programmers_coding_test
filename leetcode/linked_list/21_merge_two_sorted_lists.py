# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #         output: ListNode = ListNode()
        #         output.val = min(l1.val, l2.val)

        #         q1, q2 = collections.deque(), collections.deque()

        #         node1 = l1
        #         while node1 is not None:
        #             q1.append(node1.val)
        #             node1 = node1.next
        #         node2 = l2
        #         while node2 is not None:
        #             q2.append(node2.val)
        #             node2 = node2.next

        #         tmp = output
        #         while q1 and q2:
        #             v1, v2 = q1.popleft(), q2.popleft()
        #             tmp.val = min(v1, v2)
        #             tmp.next = ListNode()
        #             tmp = tmp.next
        #             tmp.val = max(v1, v2)
        #             tmp.next = ListNode()
        #             tmp = tmp.next

        #         return output
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
