
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def levelOrder(root):
    if root == None:
        return
    else:
        q = deque()
        q.append(root)      
        while len(q) > 0:
            n = q[0]
            print(n.data,end=' ')
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right) 
            q.popleft()    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)    
root.left.right.left = Node(70)
root.left.right.right = Node(80)  
root.right.left = Node(60)
print(levelOrder(root))              