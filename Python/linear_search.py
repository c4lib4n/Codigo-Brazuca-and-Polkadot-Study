def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 555
print("The element at index", linear_search(array, target))


