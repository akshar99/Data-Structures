# Doubly Linked List Implementation in Python

This repository contains a Python implementation of a Doubly Linked List (DLL). A DLL is a type of linked list in which each node contains a reference to both the next and the previous node in the sequence. This allows traversal of the list in both directions.

## Class Definitions

### New_Node
The `New_Node` class represents a node in the doubly linked list. Each node has three attributes:
- `value`: The data stored in the node.
- `next`: A reference to the next node in the list.
- `prev`: A reference to the previous node in the list.

### DLList
The `DLList` class represents the doubly linked list and includes the following methods:

- `__init__(self, value)`: Initializes the list with a single node containing the given value.
- `print_DLList(self)`: Prints all the values in the list.
- `append(self, value)`: Appends a node with the given value to the end of the list.
- `pop(self)`: Removes and returns the last node from the list.
- `prepend(self, value)`: Prepends a node with the given value to the beginning of the list.
- `pop_first(self)`: Removes and returns the first node from the list.
- `get_index(self, index)`: Returns the node at the given index.
- `set(self, index, value)`: Sets the value of the node at the given index.
- `insert(self, index, value)`: Inserts a node with the given value at the given index.
- `remove(self, index)`: Removes the node at the given index.

## Example Usage

Here's an example of how to use the `DLList` class:

```python
# Create a doubly linked list with an initial value
dll = DLList(1)

# Append values to the list
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

# Prepend a value to the list
dll.prepend(0)

# Set the value of the node at index 2
dll.set(2, 555)

# Insert a value at index 3
dll.insert(3, 999)

# Remove the node at index 3
dll.remove(3)

# Print the values in the list
dll.print_DLList()
