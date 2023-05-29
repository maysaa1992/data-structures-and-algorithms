class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top
        self.size = 0
        
    def getSize(self):
        return self.size
    
    def isEmpty(self):
     return self.size == 0

    def push(self,value):
       
        if  self.isEmpty():
          node = Node(value)
          self.top=node
          self.top.next=None
          self.size += 1
          return self.top.value
        else:    
            node = Node(value)
            node.next = self.top
            self.top = node
            self.size += 1
            
    
    def pop(self):
       if  self.isEmpty():
           return("This is an empty stack")
        
       else:
            temp= self.top
            self.top = temp.next
            temp.next = None
            self.size -= 1
            return temp.value

    def peek(self):
        if self.isEmpty():
            raise Exception("This is an empty stack")
             
        return self.top.value
	    
    def is_empty(self):
       
     if self.isEmpty():
         return True
     else: 
      return False

    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"    


if __name__ ==  "__main__":
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    print(stack_01)
    # print(stack_01.top.value)
    print(stack_01.is_empty()) 