"a shared stack module"

stack = []                                   # on first import
class error(Exception): pass                 # local excs, stack1.error

def push(obj):
    global stack                             # use 'global' to change
    stack = [obj] + stack                    # add item to the front

def pop():
    global stack
    if not stack:
        raise error('stack underflow')       # raise local error
    top, *stack = stack                      # remove item at front
    return top

def top():
    if not stack:                            # raise local error
        raise error('stack underflow')       # or let IndexError occur
    return stack[0]

def empty():
     return not stack           # is the stack []?
def member(obj):
    return obj in stack        # item in stack?
def item(offset):
    return stack[offset]       # index the stack
def length():
     return len(stack)          # number entries
def dump():
    print('<Stack:%s>' % stack)
    
    
    
#sample run in python interpreter
#>>> import stack
#>>> stack.push('x')
#>>> stack.push('y')
#>>> stack.top()
#y
#>>> stack.empty()
#false
#>>>stack.dump()
#<stack:['x']>
#stack.pop()
#'x'
#stack.empty()
#True
#stack.dump()
#for c in 'python': stack.push(c)
#stack.stack()
#['n', 'o', 'h', 't', 'y', 'p']
#while not stack.empty(): print(stack.pop(),end='')
#nohtyp
#stack.pop()
#stack.erro:stack underflow
#for c in 'tig': stack.push(c)
#stack.dump()
#<stack:['g''i','t']>
#for i in range(stack.length()): print(stack.item(i), end=' ')
#git


