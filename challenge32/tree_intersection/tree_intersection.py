class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)
# from challenge30.HashTable.hashtable import HashTable
from functools import reduce
from operator import add

class Node:
  '''
  A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value



class LinkedList:

    '''
    what : A class representing a singly linked list data structure
    '''
    def __init__(self):
        self.head = None


    def insert (self, value):
        '''
        insert a new node with the given value at the begining of     the linked list.
        args: value
        output : none
        
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node



class HashTable:
  '''
  what : data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
  '''
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []

    
  
  def __hash(self,key):
    '''
    A method to return the hash code of the given key
    arg : key
    output: hash code of the key(index)
    '''
    # code = 0
   
    # for char in key:
    #   code += ord(str(char)) # * weight
    # code *= 255
    # code = code % 1024
    # return code
    return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size
    return sum([ord(str(char)) for char in key]) * 283 % self.__size

  
    
  def set(self,key,value):
    '''
    Set a key-value pair in the bucket, handling collisions as              needed.
    Arguments:
    key : The key to be hashed and used as the identifier for the           value.
    value : the value that is aassociated with the key
    Returns: None
    '''
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
 

  def get(self,key):
    '''
    Retrieve the value with the given key from the hashtable
    arg : key
    return : value or None 
    '''
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  
    
    

  def has(self, key):
    '''
    A method to check if the given key exist in the hashtable.
    arg: key
    output: boolean
    '''
    # index=self.__hash(key)
    # bucket = self.__buckets[index]
    # if bucket is not None : 
    #   curr = bucket.head
    #   while curr :
    #     if curr.value[0] == key :
    #       return True
    #     curr = curr.next  
    #   return False  
    if self.get(key):
      return True
    return False  

    

  def keys(self):
    '''
    args : none
    Returns a list of all the  keys present in the Hashtable.
    '''
    return self.keys
    
    

def tree_intersection(tree_1,tree_2):
    
    '''        
    Find the common values in two binary trees using a Hashtable.

        This function takes two binary trees as input and returns a list of values that are common in both trees.

        Parameters:
            tree_1 (BinaryTree): The first binary tree.
            tree_2 (BinaryTree): The second binary tree.

        Returns:
            list: A list containing the values that are present in both `tree_1` and `tree_2`.
    '''
   
    
    common = []
    binary_tree1 = tree_1.pre_order()
    binary_tree2 = tree_2.pre_order()
    hashtable = HashTable()
    for value in binary_tree1:
        hashtable.set(key=str(value), value=value)
    for value in binary_tree2:
        if hashtable.has(str(value)):
            common.append(value)
    return common