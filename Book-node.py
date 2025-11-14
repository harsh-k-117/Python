class Node:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_featured_book(self, isbn, title):
        new_node = Node(isbn, title)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_latest