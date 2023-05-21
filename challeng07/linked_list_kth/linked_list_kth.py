class Node:
 
  def __init__( self, data, next = None ):
    self.data = data
    self.next = next


class LinkedListKth:
 
  def __init__( self ):
    self.head , self.tail = None, None
 
  def findKthFromTail( self, k ):
    if k < 0:
      return None
 
    # count k units from the self.head.
    tmp = self.head
    count = 0
    while count < k and tmp !=None:
      tmp = tmp.next
      count += 1
 
    # if the LinkedList does not contain k elements, return None
    if count < k or None == tmp:
      return None
 
    # keeping tab on the kth element from tmp, slide tmp until
    # tmp equals self.tail. Then return the kth element.
    kth = self.head
    while None != tmp.next:
      tmp = tmp.next
      kth = kth.next
 
    return kth
 
 
