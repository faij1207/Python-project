# Binary Search Algorithm
def binary_search(arr, target):
    """
    This function implements the Binary Search algorithm.
    It searches for a target element in a sorted list by repeatedly dividing the search interval in half.
    Returns the index of the target element if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Return the index of the target element
        
        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            high = mid - 1
        
        # If target is larger, ignore the left half
        else:
            low = mid + 1
    
    return -1  # Return -1 if the target is not found

# Example usage
if __name__ == "__main__":
    arr = [11, 12, 22, 25, 34, 64, 90]  # Sorted array
    target = 22
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found.")
