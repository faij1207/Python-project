# Bubble Sort Algorithm
def bubble_sort(arr):
    """
    This function implements the Bubble Sort algorithm. It repeatedly steps through
    the list, compares adjacent elements, and swaps them if they are in the wrong order.
    The process continues until the list is sorted.
    """
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Bubble Sorted Array:", sorted_arr)
