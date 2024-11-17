# Selection Sort Algorithm
def selection_sort(arr):
    """
    This function implements the Selection Sort algorithm. It repeatedly selects the smallest
    element from the unsorted part of the list and swaps it with the first unsorted element.
    """
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        min_idx = i  # Find the minimum element in the unsorted part
        for j in range(i+1, n):
            # Update min_idx if the element found is smaller than the current minimum
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = selection_sort(arr)
    print("Selection Sorted Array:", sorted_arr)
