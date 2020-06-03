# Merge Sort Algorithm


def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2

    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        elif right[0] < left[0]:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    elif right:
        result += right
    return result


arr = [10, 400, 32, 80, 900]

sorted_arr = merge_sort(arr)
print(sorted_arr)