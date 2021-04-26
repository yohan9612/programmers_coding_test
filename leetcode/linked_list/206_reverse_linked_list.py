# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        My Solving
        """

        if not head:
            return None

        output: ListNode = ListNode()
        l: List = []
        tmp = head
        while tmp is not None:
            l.append(tmp.val)
            tmp = tmp.next
        l = l[::-1]

        t = output
        for i in range(len(l)):
            t.val = l[i]
            if i != len(l) - 1:
                t.next = ListNode()
            t = t.next

        return output

        """
        Recursive
        """
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)

        """
        Iterate
        """
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
