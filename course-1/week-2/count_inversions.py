
def count_split_inv(left, right):
    """Counts 'split inversions' of array [left, right]
    
    Counts the number of inversions of concatenated array of array 'left' and
    array 'right'.

    Args:
        left: list. A sorted list from small to large.
        right: list. A sorted list from small to large.
    Returns:
        A tuple of 2 elements. First is an int, count of inversions. Second is
        a list, sorted list of concatenated [left, right].

    """    
    if left is None or right is None:
        return -1, -1
    
    i = 0
    j = 0
    count = 0
    sorted_both = []
    
    while i <= len(left) and j <= len(right):
        if i == len(left) and j == len(right):
            break
        
        # Do not update count because no elements remains in left
        if i == len(left) and j < len(right):
            sorted_both.append(right[j])
            j = j + 1
            continue

        if i < len(left) and j == len(right):
            sorted_both.append(left[i])
            i = i + 1
            continue            
        
        if left[i] < right[j] or left[i] == right[j]:
            sorted_both.append(left[i])
            i = i + 1
            continue
        
        if left[i] > right[j]:
            sorted_both.append(right[j])            
            # Adds the number of remaining elements in left
            count = count + (len(left) - i)
            j = j + 1
            continue
        
    return count, sorted_both
        
def sort_and_count(x):
    """Counts the number of inversions in list x.
    
    Args:
        x: A list
    Returns:
        A tuple of two elements. First one is number of inversions. Second one
        is sorted x.
    """
    if x is None:
        return -1, -1
    
    # Base case
    if len(x) == 1:
        return 0, x
    
    if len(x) > 1:
        split_i = len(x) // 2
        left = x[:split_i]
        right = x[split_i:]
        
        cnt_left_inv, sorted_left = sort_and_count(left)
        cnt_right_inv, sorted_right = sort_and_count(right)
        cnt_split_inv, sorted_x = count_split_inv(sorted_left, sorted_right)
        
        cnt_total = cnt_left_inv + cnt_right_inv + cnt_split_inv
        
        return cnt_total, sorted_x

def alg(file_path):
    f = open(file_path, 'r')
    x = []    
    for line in f:
        x.append(int(line))
    
    result = sort_and_count(x)
    
    return result[0]
