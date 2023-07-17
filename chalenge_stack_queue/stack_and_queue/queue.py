class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue 
        self.size=0
        
    def getSize(self):
        return self.size
    
    def isEmpty(self):
     return self.size == 0   

    def  enqueue(self,value) :
        node = Node(value)
        if self.isEmpty():
            self.front=node
            self.back=node
            self.back.next=None
            self.size += 1
            return self.back.value   
        else:  
          self.back.next= node
          self.back = node 
          self.size += 1

    def dequeue(self):
        if  self.isEmpty():
            return ("This is an empty stack")
           #raise Exception("This is an empty stack")
        
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            self.size -= 1
            return temp.value
    
    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"
    
    def peek(self):
        if self.isEmpty():
            raise Exception("This is an empty stack")
        return self.front.value
	    
    def is_empty(self):
       
     if self.isEmpty():
         return True
     else: 
      return False   


if __name__ == "__main__":
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q)
    # print(q.front.value)
    # print(q.back.value)
    # print("deleted element is ",q.dequeue())#deleted node value
    # print(q)





