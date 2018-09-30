''' bubble sort '''
def bubble(arr):
    for passnum in range(len(arr)-1, -1, -1):  #shift the largest to its repective passnum+1 pos, by flipping 2 numbers side by side
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = arr[i]

'''
time complexity = O(n)^2
space complexity = O(1)
'''
