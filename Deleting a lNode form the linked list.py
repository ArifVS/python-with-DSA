class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
n1 = Node(4)
n2 = Node(5)
n3 = Node(1)
n4 = Node(9)
n5 = Node(5)
n6 = Node(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

head = n1
curr = head
while curr!=None:
    print(curr.data,end=" ")
    curr = curr.next

curr = head
while curr!=None:
    if(curr.data==5):
        curr = curr.next
    print(curr.data,"er")
    curr = curr.next
    
    


        
