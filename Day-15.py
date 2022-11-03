class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        temp = Node(data)
        if head is None:
            head = temp
            return head
        
        currentPos = head
        while currentPos.next is not None:
            currentPos = currentPos.next
        currentPos.next = temp
    
        return head     

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  