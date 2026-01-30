# Problem 83: Find kth smallest element
# Find and fix the error

def kth_smallest(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]

