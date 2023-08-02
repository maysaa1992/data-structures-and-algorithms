class Node:
 
  def __init__( self, value, next = None ):
    self.value = value
    self.next = next


class LinkedList:
 
  def __init__( self ,head=None):
    self.head= head
      
  def Kth (self,K):
    curent = self.head
    list=[]
    while curent is not None:
     list.append(curent.value)
     curent=curent.next
    if K>len(list):
      raise Exception ("index out of rang") 
    elif K<0:
      raise Exception("index is negatev")
    else :
      list2=[]
      list2=list[::-1]
      return list2[K]
       
  # if __init__=="__main":
    
   
  
   