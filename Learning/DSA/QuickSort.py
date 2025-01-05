def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot= arr[len(arr)//2]
    left= [num for num in arr if num < pivot]
    right= [num for num in arr if num > pivot]
    middle= [num for num in arr if num == pivot]

    return quicksort(left) + middle + quicksort(right)


arr= [10,4,2,6,7,8,2,3,7,2,6,17,31]
print("befort sort :", arr)
quicksort(arr)
print("after sort :", arr)
