# implemeting stacks using list
nums = []

#push operation
nums.append(1)
print(f'Current Stack: {nums}')
#push operation
nums.append(2)
print(f'Current Stack: {nums}')
#push operation
nums.append(3)
print(f'Current Stack: {nums}')

#pop operation
popped_num  = nums.pop()
print(f'Value of popped element: {popped_num}')
print(f'Stack after pop operation: {nums}')

#get top element from stack
top  = nums[-1]
print(f'Just seeing the top element: {top}')
