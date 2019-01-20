class List:
    def __init__(self, value = None, next_ = None):
        self.value = value
        self.next_ = next_
    
    def print(self):
        cur = self
        while cur:
            print(cur.value)
            cur = cur.next_

    def append(self, value):
        cur = self
        while cur.next_:
            cur = cur.next_
        cur.next_ = List(value, None)

    
list_ = List(value=1, next_=List(value=2, next_=List(value=3)))
list_.print()

list_.append(4)
list_.print()
