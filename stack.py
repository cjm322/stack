# Basic operations: pop(), push(), peek()
# LIFO Structure: Last in, first out
# Easily implemented with arrays or linked lists

# Push():
# Put the given item to the top of the stack
# Can be done in O(1)

# Pop():
# Take the last item we have inserted to the top of the stack
# Can be done in O(1)

# Peek():
# Return the item from the top of the stack without removing it
# Can be done in O(1)

# Applications:
# - Graph algorithms: depth-first search can be implemented
# with stacks (or with recursion)
# - Finding Euler-cycles in a graph
# - Finding strongly connected components in a stack

# Stacks store temporary variables created by each function
# It keeps track of the point to which each active subroutine
# should return control when it finishes executing

class Stack:
  def __init__(self):
    self.stack = []
  
  def isEmpty(self):
    return self.stack == []
  
  def push(self, item):
    self.stack.append(item)
  
  def pop(self):
    if(self.isEmpty()):
      return self.stack
    else:
      data = self.stack[-1]
      del self.stack[-1]
      return data
  
  def peek(self):
    if(self.isEmpty()):
      return self.stack
    else:
      return self.stack[-1]
