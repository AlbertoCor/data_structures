# create nodes
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

if __name__ == "__main__":
    node1 = None
    node2 = Node("A", None)
    node3 = Node("B", node2)
    head = None
    
    # show nodes values and directions
    print(node2.data)
    print(node2.next)
    print(node3.next.data, "\n")
    
    # assign a value and direction to a node
    node1 = Node("C", node3)    
    print(node1.next.data)
    
    # create some nodes
    for count in range(1,5):
        head = Node(count,head)
        
    while head != None:
        print(head.data)
        head = head.next
    
    