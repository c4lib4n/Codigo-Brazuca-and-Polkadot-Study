from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("First element: ", queue.peek())
while not queue.is_empty():
    print(queue.dequeue())
