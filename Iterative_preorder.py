from turtle import left


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def preorder(root):
    if root == None:
        return 
    else:
        st = []
        c = root
        while c != None:
            print(c.data, end=' ')
            st.append(c.data)
            c = c.left
        while len(st) > 0:
            c = st.pop() 
            c = c.left
            while c != None:
                print(c.data)
                st.append(c.data)
                c = c.right

root = Node(10) 
root.left = Node(20) 
root.right = Node(30) 
root.left.left = Node(40) 
root.left.left.left = Node(50)
print(preorder(root))
