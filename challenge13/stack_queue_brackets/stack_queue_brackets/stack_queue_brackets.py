
def validate_brackets(string):
  """
  Validates whether or not the brackets in the string are balanced.

  Args:
    string: The string to validate.

  Returns:
    True if the brackets are balanced, False otherwise.
  """

  stack = []
  for char in string:
    if char in "()[]{}":
      if len(stack) == 0 or stack[-1] != {"(": ")", "[": "]", "{": "}"}[char]:
        return False
    #   stack.pop()

  return len(stack) == 0
if __name__=="__main__":
    string = "{}[]()"
    if validate_brackets(string):
     print("The brackets are balanced")
    else:
     print("The brackets are not balanced")