# Counting Sort Algorithm
def counting_sort(arr):
    """
    This function implements the Counting Sort algorithm. It assumes that the list contains only non-negative integers.
    It counts the occurrences of each element, then calculates the positions of each element in the sorted list.
    """
    if len(arr) == 0:
        return arr
    
    # Find the maximum element in the list
    max_val = max(arr)
    # Initialize the count array with zeros
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element in arr
    for num in arr:
        count[num] += 1
    
    # Build the output array using the count array
    output = []
    for num in range(len(count)):
        output.extend([num] * count[num])
    
    return output

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 22, 34, 12]
    sorted_arr = counting_sort(arr)
    print("Counting Sorted Array:", sorted_arr)
