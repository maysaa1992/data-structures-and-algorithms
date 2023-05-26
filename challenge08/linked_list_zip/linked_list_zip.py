class Node:
 
  def __init__( self, value, next = None ):
    self.value = value
    self.next = next


class LinkedList:
 
  def __init__( self ,head=None):
    self.head= head
      
  def zip (self,ll1,ll2):
    curent1 = ll1.head
    curent2=ll2.head
    list=[]
       
    while curent1 is not None and curent2 is not None:
     list.append(curent1.value)
     list.append(curent2.value)
     curent1=curent1.next
     curent2=curent2.next
    return list
       
  # if __init__=="__main":
    
   
  
   