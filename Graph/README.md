# Python Graph Implementation

This repository contains a basic implementation of an undirected graph in Python. The `Graph` class supports the following operations:

- **Add Vertex**: Add a vertex to the graph.
- **Add Edge**: Create an undirected edge between two vertices.
- **Remove Vertex**: Remove a vertex and all associated edges from the graph.
- **Remove Edge**: Remove an edge between two vertices.
- **Print Graph**: Display the adjacency list representation of the graph.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Code

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/graph-implementation.git
    cd graph-implementation
    ```

2. Run the Python script to see the graph operations in action:
    ```bash
    python graph.py
    ```

### Example Usage

```python
my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

my_graph.print_graph()

my_graph.remove_vertex('C')
my_graph.print_graph()
