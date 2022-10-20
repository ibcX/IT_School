# factorial: 3 = 1*2*3
# exemplu de functie recusiva
def factorial(a):
    if a < 1:
        print("Nu putem avea numere factoriale negative")
        return False
    if a == 1:
        return 1
    else:
        return (a * factorial(a-1))


fact = -10
print("Factorialul lui " + str(fact) + " este " + str(factorial(fact)))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def printTree(self, type_of_traversal):
        if type_of_traversal == "preorder":
            return self.preorder(tree.root, "")
        elif type_of_traversal == "inorder":
            return self.inorder(tree.root, "")
        else:
            print("Traversal type not supported")

    # Root->Stanga->Dreapta
    def preorder(self, start, traversal):
        if start is not None:
            traversal += (str(start.value) + "->")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    # Stanga->Root->Dreapta

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "->")
            traversal = self.inorder(start.right, traversal)
        return traversal
    #Tema:
    #Stanga->Dreapta->Root
    def postorder(self):
        pass

#        1
#      /   \
#     2     3
#    / \   / \
#    4  5  6  7
# 1->2->4->5->3->6->7->
# 4->2->5->1->6->3->7->

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#print(tree.printTree("preorder"))
print(tree.printTree("inorder"))