def swap(a, i, j):
    """Swaps a[i] and a[j].
    """
    if i == j:
        return a

    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def partition(a_1, method):
    """Partition an array for quick sort.

    Partition so that it has 3 components: subarray less than pivot, pivot, subarray greater than pivot.

    Args:
        a: A list.
        method: The method to pick pivot. This can be any value from "left", "right", or "median".

    Returns:
        Left subarray, right subarray, pivot, number of comparisons.
    """
    a = a_1.copy()

    if len(a) == 0:
        return [], [], None, 0

    l = 0
    r = len(a) - 1

    # Default method is choosing the left most element as pivot.
    if method == "left":
        pass
    if method == "right":
        swap(a, l, r)
    if method == "median_of_three":
        if len(a) % 2 == 1:
            mid = len(a) // 2
        if len(a) % 2 == 0:
            mid = len(a) // 2 - 1

        if a[mid] <= a[l] <= a[r] or a[r] <= a[l] <= a[mid]:
            pass
        if a[l] <= a[mid] <= a[r] or a[r] <= a[mid] <= a[l]:
            swap(a, l, mid)
        if a[l] <= a[r] <= a[mid] or a[mid] <= a[r] <= a[l]:
            swap(a, l, r)

    pivot = a[l]

    i = l + 1
    for j in range(l + 1, r + 1):
        if a[j] < pivot:
            swap(a, i, j)
            i = i + 1
    swap(a, l, i - 1)

    # There are 2 edge cases. The first is when pivot is the smallest element. The second is when pivot is the largest
    # element. However below slicing can address these 2 edge cases as well.
    a_left = a[l:i - 1]
    a_right = a[i:r + 1]

    return a_left, a_right, pivot, len(a) - 1


def quick_sort(a, method):
    """Main function of quick sort.
    """
    # Base case
    if len(a) == 0 or len(a) == 1:
        return a, 0

    a_left, a_right, pivot, num_compare_partition = partition(a, method)
    a_left_sorted, num_compare_left = quick_sort(a_left, method)
    a_right_sorted, num_compare_right = quick_sort(a_right, method)

    a_sorted = a_left_sorted + [pivot] + a_right_sorted
    num_compare_total = num_compare_partition + num_compare_left + num_compare_right
    return a_sorted, num_compare_total


def alg(file_path):
    f = open(file_path, 'r')
    
    input = []
    for line in f:
        input.append(int(line))
    f.close()
    num_comparison_left = quick_sort(input, "left")[1]
    num_comparison_right = quick_sort(input, "right")[1]
    num_comparison_median = quick_sort(input, "median_of_three")[1]

    return [num_comparison_left, num_comparison_right, num_comparison_median]