class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return

        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

ll = LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)

print("Given linked list")
ll.printList()

ll.reverse()

print("\nReverse linked list")
ll.printList()