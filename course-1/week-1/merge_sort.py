
def merge(left, right):
    """Merges two sorted lists.

    Args:
        left: A list. Sorted from small to large.
        Right: A list. Sorted from small to large.
    Returns:
        A merged list combining left and right. Sorted from small to large.
    """
    if left is None or right is None:
        return -1
    
    total_len = len(left) + len(right)
    
    i = 0
    j = 0
    c = [None] * total_len
    
    for k in range(total_len):
        if i >= len(left):
            c[k] = right[j]
            j = j+1
            continue
        if j >= len(right):
            c[k] = left[i]
            i = i+1
            continue
        if left[i] < right[j] or left[i] == right[j]:
            c[k] = left[i]
            i = i+1
            continue
        if left[i] > right[j]:
            c[k] = right[j]
            j = j+1
            continue
    
    return c
            

def sort(x):
    """Merge-sort a list of numbers from small to large.
    
    Args:
        x: A list.
    Returns:
        A list. Represents sorted x.
    """
    if x is None:
        return -1
    
    if len(x) == 1:
        return x
    
    split_index = len(x) // 2
    
    left = x[:split_index]
    right = x[split_index:]
    
    left_sorted = sort(left)
    right_sorted = sort(right)
    x_sorted = merge(left_sorted, right_sorted)
    
    return x_sorted