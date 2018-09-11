''' recurively '''
def binarySearch(arr, left, right, x):
    if right >= left:
        mid = int(left + (right-left)/2)
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, left, mid-1, x) #-1 because mid is not x
        else:
            return binarySearch(arr, mid+1, right, x) #+1 because mid is not x
    else:
        return -1

''' iteratively '''
def binarySearch1(arr, left, right, x):
    while left <= right:
        mid = int(left + (right - left)/2)

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid -1
    return -1

arr = [1,2,3,4,5,6]
binarySearch(arr, 0, len(arr) - 1, 5)
