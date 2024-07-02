# Queue Implementation in Python

This repository contains a Python implementation of a Queue using a linked list structure. A queue is a linear data structure that follows the First In First Out (FIFO) principle, where the first element added to the queue is the first one to be removed.

## Class Definitions

### Node
The `Node` class represents a node in the queue. Each node has two attributes:
- `value`: The data stored in the node.
- `next`: A reference to the next node in the queue.

### Queue
The `Queue` class represents the queue and includes the following methods:

- `__init__(self, value)`: Initializes the queue with a single node containing the given value.
- `print_queue(self)`: Prints all the values in the queue from first to last.
- `enqueue(self, value)`: Adds a node with the given value to the end of the queue.
- `dequeue(self)`: Removes and returns the first node from the queue.

## Example Usage

Here's an example of how to use the `Queue` class:

```python
# Create a queue with an initial value
myq = Queue(1)

# Enqueue values into the queue
myq.enqueue(2)

# Dequeue the first value from the queue
myq.dequeue()

# Print the queue
myq.print_queue()
