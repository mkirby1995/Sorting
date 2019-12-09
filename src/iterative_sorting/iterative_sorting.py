# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        smallest_element = min(arr[i:])

        # TO-DO: swap
        smallest_index = arr.index(smallest_element)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        for i in range(0, len(arr) - i - 1):
            print(arr)
            a = arr[i]
            b = arr[i + 1]
            print("A:", a, "\tB:", b)
            if a > b:
                a_index = arr.index(a)
                b_index = arr.index(b)
                arr[a_index] = b
                arr[b_index] = a
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    n = max(arr) + 1
    count_array = [0] * n
    for i in range(len(count_array)):
        if i in arr:
            count_array[i] += 1
    for i in range(1, len(count_array) - 1):
        count_array[i + 1] += count_array[i]
    sorted_arr = [0] * (len(arr) + 1)
    for i in arr:
        #print("Arr value:", i)
        #print("Count array value at index(", i, "):", count_array[i])
        sorted_arr[count_array[i]] = i
        count_array[i] -= 1
    if 0 in arr:
        return sorted_arr
    else:
        sorted_arr.remove(0)
        return sorted_arr
