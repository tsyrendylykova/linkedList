class Node:
    def __init__(self, value = None, next_ = next):
        self.value = value
        self.next_ = next_

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def clear(self):
        self.__init__()

    def push(self, value):
        if self.head is not None:
            self.head = Node(value, self.head)
        else:
            self.head = Node(value, None)
            self.tail = self.head

    def print_(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next_

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next_
            curr_node.next_ = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        
    def print_reversed(self):
        self.reverse()
        self.print_()