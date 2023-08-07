from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.put(item)

    def pop(self):
        if self.queue.empty():
            return None
        temp_queue = Queue()
        while self.queue.qsize() > 1:
            temp_queue.put(self.queue.get())
        popped_item = self.queue.get()
        self.queue = temp_queue
        return popped_item

# Test
stack = StackUsingQueue()
stack.push(1)
print(stack.pop())  # Output: 1

stack.push(2)
print(stack.pop())  # Output: 2

stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: None
