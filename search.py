import math
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def search(root,x):
    flag = False
    if root == None:
        return   
    else:
        if root.data == x:
            flag =True
        ls = search(root.left,x)
        rs = search(root.right,x)
        return
    if flag:
        return True
    else:
        return False         

    
root = Node(10) 
root.left = Node(20) 
root.right = Node(30) 
root.left.left = Node(40) 
root.left.left.left = Node(50)
print(search(root,0))                 