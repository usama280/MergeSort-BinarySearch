def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
        
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    #print(f'Left: {left}')
    #print(f'Right: {right}')
    return merge(left, right)


def merge(left, right):
    result = []
    i,j = 0, 0

    while i<len(left) and j<len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    #print(f'Result: {result}')
    return result

