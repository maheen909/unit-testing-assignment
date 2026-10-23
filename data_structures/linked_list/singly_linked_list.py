class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def delete_head(self):
        if self.is_empty():
            raise IndexError("List is empty")
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def delete_tail(self):
        if self.is_empty():
            raise IndexError("List is empty")
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self._size -= 1
            return data

        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        self._size -= 1
        return data

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self._size