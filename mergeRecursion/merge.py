def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    # divide array in two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # merge the two sorted halves
    merged_arr = merge(left_half, right_half)

    return merged_arr


def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0

    # merge the two sorted halves into one array
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # add the remaining elements to the merged array
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged


# test
arr = [5, 2, 1, 3, 6, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)
