# Stack Implementation in Python

This repository contains a Python implementation of a Stack using a linked list structure. A stack is a linear data structure that follows the Last In First Out (LIFO) principle, where the last element added to the stack is the first one to be removed.

## Class Definitions

### Node
The `Node` class represents a node in the stack. Each node has two attributes:
- `value`: The data stored in the node.
- `next`: A reference to the next node in the stack.

### Stack
The `Stack` class represents the stack and includes the following methods:

- `__init__(self, value)`: Initializes the stack with a single node containing the given value.
- `print_stack(self)`: Prints all the values in the stack from top to bottom.
- `push(self, value)`: Pushes a node with the given value onto the top of the stack.
- `pop(self)`: Pops the top node from the stack and returns its value.

## Example Usage

Here's an example of how to use the `Stack` class:

```python
# Create a stack with an initial value
mystack = Stack(1)

# Push values onto the stack
mystack.push(2)
mystack.push(3)
mystack.push(4)

# Print the stack
mystack.print_stack()

# Pop the top value from the stack
mystack.pop()

# Print the stack again
mystack.print_stack()
