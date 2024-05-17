from Node import Node

class SortedSLL:
    def __init__(self):
        self.head = None
        self.n = 0

    def insert(self, data):
        self.n += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        elif data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            # print('inserted:', data)

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()