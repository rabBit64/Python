class Node: 
    def __init__(self,value): 
        self.value = value
        self.left = None
        self.right = None


def preorder(object):
    
    if object== None:
        return None
    
    if root:
        preorder(object.left)
        print object.value
        preorder(object.right)
        

def inorder(object):
    
    if object== None:
        return None
    
    if root:
        print object.value
        inorder(object.left)
        inorder(object.right)
        
def postorder(object):
    
    if object== None:
        return None
    
    if root:
        postorder(object.left)
        postorder(object.right)
        print object.value

if __name__ =="__main__":
    root = Node(15)
    root.left = Node(1)
    root.right = Node(37)
    root.left.left = Node(61)
    root.left.right = Node(26)
    root.right.left = Node(59)
    root.right.right = Node(48)
    
    print "Preorder Traverse"
    preorder(root)
    print "Inorder Traverse"
    inorder(root)
    print "Postorder Traverse"
    postorder(root)
