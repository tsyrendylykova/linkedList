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
            for elem in other:
                cur.next_ = List(elem)
                cur = cur.next_
        return self

    @property
    def _value(self):
        return self.value

    @_value.setter
    def _value(self, value):
        self.value = value

    def __iter__(self):
        cur = self
        while cur:
            yield cur.value
            cur = cur.next_

    def print_reversed(self):
        reversed_list = None
        cur = self
        while cur:
            reversed_list = List(cur.value, next_ = reversed_list)
            cur = cur.next_
        reversed_list.print()

    def print_reversed_recursive(self):
        if self.next_ is None:
            print(self.value, end = " ")
            return
        else:
            self.next_.print_reversed_recursive()
            print(self.value, end = " ")

def main():
    list_ = List(value=1, next_=List(value=2, next_=List(value=3)))
    list_.print()

    list_.append(4)
    list_.print()

    tail = List(value=5, next_=List(value=6))
    list_ += tail

    list_.print()

    tail._value = 0
    tail.print()
    list_.print()
            
    list_ += [7, 8]
    list_.print()

    for elem in list_:
        print(2 ** elem, end=" ")
    print("")

    list_.print_reversed()

    list_.print_reversed_recursive()
    print("")


if __name__ == '__main__':
    main()