def selectSort(arr):
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
                if i != minIndex:
                    arr[j], arr[minIndex] = arr[minIndex], arr[i]

    return arr
