class Node:
    def __init__(self,k):
        self.k = k
        self.left = None
        self.right = None

def size(root):
    if root == None:
        return 0
    else:
        ls = size(root.left) 
        rs = size(root.right)
        return ls + rs + 1
           
        
root = Node(10) 
root.left = Node(20) 
root.right = Node(30) 
root.left.left = Node(40) 
root.left.left.left = Node(50)
print(size(root))