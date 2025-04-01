def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    print("Original array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)