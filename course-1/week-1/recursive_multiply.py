
def recursive_multiply(x, y):
    """
    x, y are positive integers
    """
    len_x = len(str(x))
    len_y = len(str(y))
    
    if x is None or len_x == 0 or y is None or len_y == 0:
        return None
    
    # base case
    if len_x == 1 and len_y == 1:
        return x * y
    
    m = len_x // 2
    a = int(str(x)[:len_x-m])
    if len_x > 1:
        b = int(str(x)[len_x-m:])
    elif len_x == 1:
        b = 0
    else:
        b = None
            
    n = len_y // 2
    c = int(str(y)[:len_y-n])
    if len_y > 1:
        d = int(str(y)[len_y-n:])
    elif len_y == 1:
        d = 0
    else:
        d = None
        
    result = 10**(m+n) * recursive_multiply(a, c) + 10**m * recursive_multiply(a, d) \
            + 10**n * recursive_multiply(b, c) + recursive_multiply(b, d)
    return result

def alg(file_path):
    f = open(file_path, 'r')
    a = []
    for line in f:
        a.append(int(line))
    
    x = a[0]
    y = a[1]
    
    result = recursive_multiply(x, y)
    return result
    