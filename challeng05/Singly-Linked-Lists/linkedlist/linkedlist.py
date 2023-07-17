class Node : #value next
    def __init__(self, value,_next=None):
        self.value = value
        self.next = _next



class LinkedList:
    def __init__(self,head=None):
        self.head = head
        

    def traverse_return(self,x) :
        current = self.head
        while current:
            
            if current.value== x:
             return True
            else:
             current = current.next    
        return False  

    def traverse_print(self) :
        current = self.head
        str_list=""
        while current:
            str_list += str(current.value) +"->"
            current = current.next
        str_list +="None"    
        return str_list

    def insert (self, value) : 
         # insert vs append 
         new_node = Node(value)
         new_node.next = self.head
         self.head = new_node

         
if __name__ == '__main__':

    node_c=Node ("{ c }")
    #print(node_c.value)
    node_b=Node ("{ b }",node_c)
    node_a=Node ("{ a }",node_b)
    print(node_a.value) 
    li_=LinkedList(node_a)
    print (li_.traverse_return("{ k }"))
    print(li_.head)
    print(li_.traverse_print()) 
    
   