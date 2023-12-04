class Node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node: %s>"%self.data
    

class LinkedList:

    def __init__(self):
        self.head = None

    def isempty(self):
        self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count


if __name__ == '__main__':
    n1 = Node(10)
    n = Node(5)
    print(n1)
    n2 = Node(20)
    n1.next_node = n2
    print(n1.next_node)
    l = LinkedList()
    l.head = n
    print(l.size())
