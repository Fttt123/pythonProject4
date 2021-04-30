import stack

def ic(x: str):
    stack.clear()
    if x == '':
        return False
    for brace in x:
        if brace in '()':
            if brace in '(':
                stack.push(brace)
            else:
                if stack.is_empty():
                    return False
                left = stack.pop()
                if left == '(':
                    right = ')'
                if brace != right:
                    return False
    return stack.is_empty()
