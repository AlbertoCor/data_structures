from node import Node

class SinglyLinkedlist:
    # init class
    def __init__(self):
        self.tail = None
        self.size = 0
    
    # create function for add items on nodes
    def append(self, data):
        node = Node(data)
        
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            
            while current.next:
                current = current.next
                
            current.next = node
        
        self.size += 1
        
    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail
        
        while current:
            val = current.data
            current = current.next
            yield val
            
    def delete(self, data):
        current = self.tail
        previous = self.tail
        
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else: 
                    previous == current.next
                    self.size -= 1
                    return current.data
                
            previous = current
            current = current.data
            
    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"data {data} found!")
                
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
        

if __name__ == "__main__":
    # create linked list
    words = SinglyLinkedlist()
    # append data to a nodes
    words.append("egg")
    words.append("Ham")
    words.append("spam")
    current = words.tail
    
    # order data in nodes
    while current:
        print(current.data)
        current = current.next
    
    # order data in nodes  
    for word in words.iter():
        print(word)
    
    # look for a value in linked list
    words.search("spam")
    words.search("juice")
        
    # clear values in nodes
    words.clear()
    
    # order data in nodes but there's nothing by cleared not start while loop
    while current:
        print(current.data)
        current = current.next
    
        