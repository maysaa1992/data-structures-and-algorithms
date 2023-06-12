# from assets import Node,Queue,Stack
class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root=None
     
    def find_max_value(self):
        """Finds the maximum value stored in a binary tree.


        Returns:
            The maximum value stored in the tree.

        Raises:
            TypeError: If `tree` is not a binary tree.
        """

        
        max_value = self.root.value

        def _walk(root):
                    
                    if max_value <self.root.value:
                        max_value = self.root.value
                    if self.root.left:
                        _walk(self.root.left)
                    if self.root.right:
                        _walk(self.root.right)

                    _walk(self.root)
        return max_value


 
        
                
        
if __name__ == "__main__":
  tree = BinarySearchTree()
  tree.root= Tnode(10)
  tree.root.left=Tnode(20)
  tree.root.right = Tnode(70)
  tree.root.left.left = Tnode(30)
  tree.root.left.right = Tnode(40)
  tree.root.right.right = Tnode(90)
  tree.root.right.right = Tnode(100)


  
  print (tree.find_max_value() )
