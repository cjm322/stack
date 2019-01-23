from stack import Stack

s = Stack()

def clear_stack(stack):
  if(stack.isEmpty()):
    return stack
  else:
    stack.pop()
    clear_stack(stack)

for i in range(1, 11):
  s.push(i)

print("Last item in stack: %i" % s.peek())
print("Clearing stack...")
clear_stack(s)
print("Stack is empty?")
print(s.isEmpty())
