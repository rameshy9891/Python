class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    def reverse_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse_list(slow)

    while second_half:
        if head.val != second_half.val:
            return False
        head = head.next
        second_half = second_half.next

    return True

# Test: Assuming you have a linked list defined.
# Example usage: is_palindrome(head)
