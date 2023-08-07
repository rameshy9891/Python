class QueueUsingStack:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack.pop()
        return None

# Test
queue = QueueUsingStack()
queue.enqueue(1)
print(queue.dequeue())  # Output: 1
queue.enqueue(2)
print(queue.dequeue())  # Output: 2
queue.enqueue(3)
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: None
