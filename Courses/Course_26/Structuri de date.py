#list
from collections import deque

queue = deque([1, 2, 3])
print(queue)

queue.appendleft(5)
print(queue)
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack")
print(stack)

stack.pop()
print("Stack after a pop")
print(stack)
stack.pop()
stack.pop()


#stack.pop() // error stack underflow = poping from a empty list
#stack overflow = error when pushing over the max capacity of a stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    #demonstram parcurgerea unei liste inalnuite simple
    def printLinkedList(self):
        current_nod = self.head
        while current_nod is not None:
            print(current_nod.data)
            current_nod = current_nod.next

    def InsertAtBegin(self, new_data):
        New_node = Node(new_data)
        New_node.next = self.head
        self.head = New_node
    def InsertAtTheEnd(self,new_data):
        #homework
        pass
    def RemoveNodeAfterValue(self,data):
        global prev
        curr_nod = self.head
        if curr_nod is not None:
            if curr_nod.data == data:
                self.head = curr_nod.next
                curr_nod = None
                return

        while curr_nod is not None:
            if curr_nod.data == data:
                break
            prev = curr_nod
            curr_nod = curr_nod.next

        if curr_nod == None:
             print("data not found")
             return
        prev.next = curr_nod.next
        curr_nod = None

    def InsertAfterKey(self, key, new_data):
        #homework
        pass
list = LinkedList()
list.head = Node("Sergiu")
n1 = Node("Sebastian")
n2 = Node("Victor")

#inlantuim
list.head.next = n1
n1.next = n2
list.printLinkedList()

list.InsertAtBegin("Armando")
print("New list : ")
list.printLinkedList()

list.RemoveNodeAfterValue("Victor")
print("New list:")
list.printLinkedList()

