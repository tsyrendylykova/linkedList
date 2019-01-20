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