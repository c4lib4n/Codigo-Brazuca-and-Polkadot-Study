class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkdeList:
    def __init__(self):
        self.head = None

    def append(self, data):
        #new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")

ll = LinkdeList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()

