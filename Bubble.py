#Bubble Sort algorithm

nums = [10, 34, 88, 91, 2, 3]

def bubble_sort(arr):
    for i in range(len(arr)):
        for index in range(len(arr) - i - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index+1] = arr[index + 1], arr[index]


bubble_sort(nums)
print(nums)

