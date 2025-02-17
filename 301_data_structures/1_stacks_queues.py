"""
Stacks
* LIFO
"""
# Peek
# Push
# Pop
# is_empty

stack = ["a", "b", "c", "d", "e"]
print(f"STACK: {stack}")
# Peek
peek = stack[-1]
print(f"peek: {peek}")

# Push
stack.append("f")
stack.append("g")
print(f"push f and g: {stack}")

# Pop
pop = stack.pop()
print(f"pop: {pop}")

# is_empty
is_empty = len(stack) < 1
print(f"is_empty: {is_empty}\n\n")

"""
Queues
* FIFO
"""
# Peek
# Enqueue similar to Push
# Dequeue similar to Unshift
# is_empty

"""
In Python there are 2 ways, either we follow the official tutorial and use *collections > deque*.
Or we implement our own queue using Linked Lists to avoid the lists inefficiencies.
I'll do both here to get a better sense.
"""

## FIRST VERSION - tutorial ##
from collections import deque
queue = deque(["Here", "we", "go"])
print(f"FIRST QUEUE: {queue}")

# Peek
peek = queue[-1]
print(f"peek: {peek}")

# Enqueue - add at the end
queue.append("again")
queue.append("!")
print(f"Enqueue: {queue}")

# Dequeue
dequeue = queue.popleft()
print(f"Dequeue: {dequeue}")
print(f"After dequeue: {queue}")

dequeue = queue.popleft()
print(f"One more time, let's dequeue: {dequeue}")
print(f"After dequeue: {queue}")

# is_empty
is_empty = len(queue) < 1
print(f"is_empty: {is_empty}\n\n")

## SECOND VERSION - Linked Lists ##
from typing import Optional

class Node:
    def __init__(self, value: str, next_node: Optional['Node'] = None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        """
        Representation - Represent Node as a string.
        """
        return f"Node(value={self.value})"
    
class Queue:
    def __init__(self):
        self.first_element: Optional[Node] = None
        self.last_element: Optional[Node] = None
        self.length: int = 0

    def is_empty(self) -> bool:
        return True if self.length < 1 else False

    def peek(self) -> Optional[str]:
        return self.first_element.value if not self.is_empty() else None
    
    def enqueue(self, value: str):
        node = Node(value)

        if self.length:
            self.last_element.next_node = node
        else:
            self.first_element = node

        self.last_element = node
        self.length += 1
    
    def dequeue(self) -> Optional[str]:
        peek = self.peek()

        if peek:
            self.first_element = self.first_element.next_node

            if self.length == 1:
                self.last_element = None

            self.length -= 1

        return peek
    
    def __repr__(self):
        values = []
        current = self.first_element
        while current:
            values.append(current.value)
            current = current.next_node
        return ", ".join(values) if len(values) else "Empty queue"

queue = Queue()
print(f"Initial queue: {queue}")
print(f"Is empty: {queue.is_empty()}")
queue.enqueue("My")
print(f"After enqueue: {queue}")
queue.enqueue("second")
queue.enqueue("queue")
queue.enqueue("!")
print(f"After 3 enqueues: {queue}")
print(f"Is empty: {queue.is_empty()}")
print(f"peek: {queue.peek()}\n")

for _ in range(queue.length):
    print(f"Dequeuing: {queue.dequeue()}")
    print(f"Current queue: {queue} - length: {queue.length}")

print(f"Dequeue after for loop: {queue.dequeue()}")
print(f"Length: {queue.length}")
