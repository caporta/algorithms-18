class ListNode():
    """
    Implementation of a singly-linked list
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class HashTableApproach():
    def has_cycle(self, head: ListNode) -> bool:
        if not head:
            return False

        # set > list improves membership lookup performance
        # as it is backed by a hash table
        visited = {head}
        while head.next is not None:
            if head.next in visited:
                return True

            visited.add(head.next)
            head = head.next

        return False

    # TIME COMPLEXITY: O(n) — we visit each of the n elements in the list at most once.
    # Adding node to hash table costs only O(1)

    # SPACE COMPLEXITY: O(n) — The space depends on the number of elements added
    # to the hash table, which contains at most n elements


class TwoPointersApproach():
    """
    Implementation leverages Floyd's Cycle-Finding Algorithm
    (also called "tortoise and the hare algorithm") for
    improvement in space complexity from O(n) -> O(1)
    """
    def has_cycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

    # TIME COMPLEXITY:
        # _list has no cycle_: O(n)
        # _list has cycle_: O(n) — O(n + k) where k is maximum distance "cyclic length k"
    # SPACE COMPLEXITY: O(1) — We only use two nodes
