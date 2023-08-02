class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def append1(self, new_data):
        str_list = "head -> " + str(self.head.value) + " -> "
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
            str_list += str(last.value) + " -> "
        last.next = new_node
        str_list += str(new_data) + " -> X"
        return str_list
    
    def insertAfter(self, prev_node, new_data):
        str_list = "head -> " 
        if prev_node is None:
            print("The given previous node must be in the LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        current = self.head
        while current:
            str_list += str(current.value) +" ->"
            current = current.next
        str_list +="X"    
        return str_list
      
    
    def insertBefore(self, befo_node, new_data):
        str_list = "head -> " 
        new_node = Node(new_data)

        if befo_node is None:
            print("The given befor node must be in the LinkedList.")
            return
        current = self.head    
        while current:
         if current.next==befo_node:
             current.next=new_node
             new_node.next=befo_node
        
        current_print = self.head
        while current:
            str_list += str(current_print.value) +"->"
            current_print = current_print.next
        str_list +="X"    
        return str_list
       
if __name__ == '__main__':
    node_c = Node(2)
    node_b = Node(3, node_c)
    node_a = Node(1, node_b)
    li_ = LinkedList(node_a)
    # print(li_.append1(5))
    # print(li_.insertAfter(node_b, 5))
    print(li_.insertBefore(node_b, 5))