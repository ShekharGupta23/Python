# Class to represent node of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to define linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next

# Creating a linked list and adding elements to it
ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(85)

print ("Given Linked List:")
ll.printList()

prev = None
curr = ll.head
while(curr is not None):
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
ll.head = prev

print ("\nReversed Linked List:")
ll.printList()