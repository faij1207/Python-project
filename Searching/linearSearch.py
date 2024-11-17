# Linear Search Algorithm
def linear_search(arr, target):
    """
    This function implements the Linear Search algorithm.
    It searches for a target element in the list by checking each element sequentially.
    Returns the index of the target element if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target is not found

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found.")
