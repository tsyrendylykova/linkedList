class List:
    def __init__(self, value = None, next_ = None):
        self.value = value
        self.next_ = next_
    
    def print(self):
        cur = self
        while cur:
            print(cur.value, end=" ")
            cur = cur.next_
        print("", flush = True)

    def append(self, value):
        cur = self
        while cur.next_:
            cur = cur.next_
        cur.next_ = List(value, None)

    def __iadd__(self, other):
        if other is None:
            return self
        cur = self
        while cur.next_:
            cur = cur.next_
        if isinstance(other, List):
            cur.next_ = List(other.value)
            cur = cur.next_
            while other.next_:
                other = other.next_
                cur.next_ = List(other.value)
                cur = cur.next_
        elif isinstance(other, list):
            # todo
            print("todo")
        return self

    @property
    def _value(self):
        return self.value

    @_value.setter
    def _value(self, value):
        self.value = value


    
list_ = List(value=1, next_=List(value=2, next_=List(value=3)))
list_.print()

list_.append(4)
list_.print()

tail = List(value=5, next_=List(value=6))
list_ += tail

list_.print()

tail._value = 0
tail.print()
              
