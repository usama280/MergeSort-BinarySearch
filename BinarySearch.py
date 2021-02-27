def binary_search(arr, val):
    mid = len(arr)//2
    
    if arr[mid] == val:
        return mid
    elif len(arr) == 1: #doesnt exist
        return -1


    elif arr[mid] > val:
        mid -= binary_search(arr[:mid], val)
        return mid
    else:
        mid += binary_search(arr[mid:], val)
        return mid

