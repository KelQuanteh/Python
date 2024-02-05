def merge_sort(array):
    # Base case: if the length of the array is 0 or 1, it is already sorted
    # and there's nothing to do.
    if len(array) <= 1:
        return
    
    # Find the middle point of the array.
    middle_point = len(array) // 2
    
    # Divide the array into two halves: left_part and right_part.
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively call merge_sort on each half to sort them.
    merge_sort(left_part)
    merge_sort(right_part)

    # Initialize indices for the left_part, right_part, and the sorted array.
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the sorted left_part and right_part back into the original array.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements in the left_part into the original array.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Copy any remaining elements in the right_part into the original array.
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    # Example usage
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    
    # Sort the array using merge_sort function.
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))