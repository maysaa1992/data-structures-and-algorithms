# from assets import Node,Queue,Stack
class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root=None
     
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


 
        
                
        
if __name__ == "__main__":
  tree = BinarySearchTree()
  tree.root= Tnode(10)
  tree.root.left=Tnode(20)
  tree.root.right = Tnode(250)
  tree.root.left.left = Tnode(30)
  tree.root.left.right = Tnode(200)
  tree.root.right.right = Tnode(90)
  tree.root.right.right = Tnode(100)


  
  print (tree.find_maximum_value() )
