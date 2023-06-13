# from assets import Node,Queue,Stack
class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None
    # children = []


class BinarySearchTree:
  def __init__(self):
    self.root=None
  def pre_order(self):
    list=[]

    def _walk(root):
      #root
      print(root.value)
      list.append(root.value)
      #left
      if root.left :
        _walk(root.left)
        
      #right
      if root.right :
        _walk(root.right)     

    _walk(self.root)
    return list 

  def in_order(self):
    list=[]
    def _walk(root):
      
      #left
      if root.left :
        _walk(root.left)
        
      #root
      print(root.value)
      list.append(root.value)

      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return list 
    
  def post_order(self):
     list=[]
     def _walk(root):
      
      #left
      if root.left :
        _walk(root.left)

      #right
      if root.right :
        _walk(root.right)
        
      print(root.value)
      list.append(root.value)

     _walk(self.root)
     return list 
    
  def find_maximum_value(self) :
        """this method is used to find the highest number in tree and return it"""

        max_value = self.root.value

        def _walk(root):
               nonlocal max_value
               if max_value < root.value:
                   max_value = root.value
               if root.left:
                 _walk(root.left)
               if root.right:
                  _walk(root.right)

        _walk(self.root)
        return max_value 
     
class Search_Tree(BinarySearchTree)  :
    def Add (self,val) :
         if val < self.root.value:
            if self.left is None:
               self.left = Tnode(val)
               return "add to left"
            else:
               self.left.Add(val)
               return "add to left"
         elif val > self.root.value:
               if self.right is None:
                  self.right = Tnode(val)
                  return "add to right "
               else:
                  self.right.Add(val)
                #   return "add to right"
       
             
    def Contains(self,val):
        if val < self.root.value:
            if (self.left == None):
                self.left.Contains(val)
                return False
        elif val >self.root.value:
            if (self.right == None):
                self.right.Contains(val)
                return False
        else:
            return True
          
         
        
                
        
if __name__ == "__main__":
  tree = BinarySearchTree()
  tree.root= Tnode(10)
  tree.root.left=Tnode(20)
  tree.root.right = Tnode(90)
  tree.root.left.left = Tnode(30)
  tree.root.left.right = Tnode(40)
  tree.root.right.left = Tnode(60)
  Tnode(20).left=Tnode(30)
  # print(Tnode(20).left)
  # print(tree.breadth_first())
  # tree.pre_order() 
  # print("###############")
  # tree.in_order()
  # print("###############")

  # tree.post_order()
  print (tree.find_maximum_value() )