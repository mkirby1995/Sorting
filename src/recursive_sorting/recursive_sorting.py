# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    left = 0
    right = 0

    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1

    merged_arr += arrA[left:]
    merged_arr += arrB[right:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
