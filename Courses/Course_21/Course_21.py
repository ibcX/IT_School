class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def insert_at_beginning(self, new_data):
        new_head_node = Node(new_data)
        new_head_node.next = self.head
        self.head = new_head_node

    # ############################  Homework    ######################
    def insert_at_the_end(self, new_data):
        new_tail = Node(new_data)
        current_node = self.head

        while current_node is not None:
            if current_node.next is None:
                current_node.next = new_tail
                break
            current_node = current_node.next

    def insert_after_key(self, key, new_data):
        new_node = Node(new_data)
        current_node = self.head

        while current_node is not None:
            if current_node.data == key:
                new_node.next = current_node.next
                current_node.next = new_node
                break
            current_node = current_node.next

        if current_node is None:
            print("\nNode not found!")
            return

    ##################################################################

    def remove_node_after_value(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                break
            previous = current_node
            current_node = current_node.next

        if current_node == None:
            print("Data not found!")
            return

        previous.next = current_node.next
        current_node = None


list = linked_list()

list.head = Node("Node_1")
node_2 = Node("Node_2")
node_3 = Node("Node_3")
node_4 = Node("Node_4")

list.head.next = node_2
node_2.next = node_3
node_3.next = node_4

list.print_linked_list()
print("\nNew head node inserted: ")
list.insert_at_beginning("New_head_node")
list.print_linked_list()

list.remove_node_after_value("Node_3")
print("\nNode_3 deleted: ")
list.print_linked_list()

list.insert_at_the_end("New_tail")
print("\nNew tail node inserted: ")
list.print_linked_list()

list.insert_after_key("Node_2", "Node_2.1")
print("\nNode 2.1 inserted after Node_2: ")
list.print_linked_list()
