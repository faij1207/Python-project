# Insertion Sort Algorithm
def insertion_sort(arr):
    """
    This function implements the Insertion Sort algorithm. It builds the final sorted array one item at a time.
    It takes each element from the unsorted part and inserts it into its correct position in the sorted part.
    """
    n = len(arr)
    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insertion_sort(arr)
    print("Insertion Sorted Array:", sorted_arr)
