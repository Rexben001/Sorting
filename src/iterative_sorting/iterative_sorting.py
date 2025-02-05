# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arrLength = len(arr) - 1
    for i in range(arrLength):
        for j in range(arrLength - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr
    
    
    return arr


# selection_sort([1, 4, 2])
# bubble_sort([1, 2, 4, 5, 6, 0, 30, 23, 21])
