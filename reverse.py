class ListNode():
    """
    Implementation of a singly-linked list
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class IterativeApproach():
    def reverse(self, head: ListNode) -> bool:
        prev = None
        current = head
        while current is not None:
            next_tmp = current.next
            current.next = prev
            prev = current
            current = next_tmp

        return prev

    # TIME COMPLEXITY: O(n) — visits every node

    # SPACE COMPLEXITY: 0(1)

class RecursiveApproach():
    def reverse(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

    # TIME COMPLEXITY: O(n) — visits every node

    # SPACE COMPLEXITY: 0(n) — call stack
