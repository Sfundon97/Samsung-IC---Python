#Stack
stack = []

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop

push(stack, 'A')
print(stack)
push(stack, 'B')
print(stack)
pop(stack)
print(stack)
push(stack, 'C')
print(stack)