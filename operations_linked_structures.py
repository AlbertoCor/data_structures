
# methods class single linked list

from node import Node

head = None
new_item = "z"

for count in range(1,6):
    head = Node(count, head)
    
# while head != None:
#     print(head.data)
#     head = head.next

# while probe != None:
#     print(probe.data)
#     probe = probe.next
    
probe = head
target_item = 3
# while probe != None and target_item != probe.data:
#     probe.next

if probe != None:
    print(f"Target item {target_item} has been found")    
else:
    print(f"Target item {target_item} is not in the linked list")
    

# insert new element or node at begining of the list
if __name__ == "__main__":
    head = Node("F", head)
    new_node = Node("k")
    
    if  head is None:
        head == new_node
    else: 
        probe = head
        while probe.next != None:
            probe = probe.next
        probe.next = new_node
        
        
# delete an node of a list

remove_item = head.data
head = head.next
print(remove_item)


# delete final item 
remove_item = head.data
if head.next is None:
    head = None
else: 
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None
    
print(removed_item)


# specified item to insert
new_tem = input("Enter new item: ")
index = int(input("Enter position to insert the new item: "))
if head is None or index < 0:
    head = Node("Py", head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)
    
# spicified item to remove
index = 3

if index <= 0 or head.next is None:
    remove_item = head.data
    head = head.next
    print(remove_item)
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next
    print(remove_item)
    
    
    