class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class StackUsingLinkedList:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = ListNode(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            popped_item = self.head.val
            self.head = self.head.next
            return popped_item
        return None

# Test
stack = StackUsingLinkedList()
stack.push(1)
print(stack.pop())  # Output: 1
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: None
