#middle of linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
#counting number of Nodes present in the linked list
count = 0
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
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
    count+=1
    print(curr.data,end=" ")
    curr = curr.next
print(count)
curr = head
for i in range(count//2):
    curr = curr.next
print(curr.data)
    
    


        
