''' recursion '''
def subsetSum(path, array, target):
    if sum(path) == target:
        print(path)
        return
    for i in range(0, len(array)):
        subsetSum(path+[array[i]], array[i+1:], target)

subsetSum([], [3, 34, 4, 12, 5, 2], 9)

''' dynamic programming '''
def dynamicSubsetSum(path, array, target):
    subset = [["" for _ in range(target+1)] for i in range(len(array+1))]

    for i in range(len(array)): #given array
        subset[i][0] = True

    for i in range(1, target+1):
        subset[0][i] = False

    for i in range(1, len(array)+1):
        for j in range(1, target+1):
            subset[i][j] = subset[i-1][j]

            if subset[i][j] == False and j >= array[i-1]:
                subset[i][j] = subset[i][j] or subset[i-1][j-array[i-1]]

    return subset[-1][-1]
        

    
