class New_Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
 
class DLList:
    def __init__(self, value):
        temp = New_Node(value)
        self.head = temp
        self.tail = temp
        self.length = 1
 
    def print_DLList(self):
        temp = self.head
 
        while temp:
            print(temp.value)
            temp = temp.next
 
    def append(self, value):
        temp = New_Node(value)
 
        if self.length == 0:
            self.head = temp
            self.tail = temp
       
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        temp.next = None
 
        self.length +=1
 
    def pop(self):
        if self.length==0:
            print("empty")
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -=1
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return None


    def prepend(self, value):
        newnode = New_Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            self.length +=1
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get_index(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head

        if index <self.length/2:
            for _ in range(index):
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        temp = self.get_index(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or self.length < index:
            return False
        if index ==0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = New_Node(value)
        temp = self.get_index(index - 1)
        after = temp.next
        new_node.next = after
        new_node.prev = temp
        temp.next = new_node
        after.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 and index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        node_a = self.get_index(index - 1)
        node_b = node_a.next
        node_c = node_b.next
        node_a.next = node_c
        node_c.prev = node_a
        node_b.next = node_b.prev = None

        return True
        

dll = DLList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.prepend(0)
dll.set(2,555)
dll.insert(3,999)
dll.remove(3)
dll.print_DLList()
