# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        My Solving
        """
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        tmp1, tmp2 = reverse(l1), reverse(l2)

        n1, n2 = 0, 0
        while tmp1:
            n1 = n1 * 10 + tmp1.val
            tmp1 = tmp1.next
        while tmp2:
            n2 = n2 * 10 + tmp2.val
            tmp2 = tmp2.next

        num = n1 + n2
        output = ListNode()
        t = output
        tmp = num
        for i in range(len(str(num))):
            t.val = tmp % 10
            tmp //= 10
            if i != len(str(num)) - 1:
                t.next = ListNode()
            t = t.next

        return output

        """
        Book
        """


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def toList(self, node: List) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        resultStr = int(''.join(str(e) for e in a)) + \
            int(''.join(str(e) for e in b))
        return self.toReverseLinkedList(str(resultStr))

        """
        Full Adder
        """
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
