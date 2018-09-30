'''
mergseSort is recursive
It is a divide and conquer algorithm
Very efficient for large data sets

It does log(n) merge steps because each merge step doubles the list size
Does n work for each merge step because it must look at every item
Runs in O(nlog(n))
'''
def merge_sort(A):   #where A is the list to be sorted
    merge_sort2(A, 0, len(A)-1)
    return A

def merge_sort2(A, first, last): #first = index of the start, last = index of the end
    if first < last: #if there is more than one item in the list
        middle = (first+last)//2     
        merge_sort2(A, first, middle)  #call mergeSort2 on the first and second half till each there is only one element
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    L = A[first: middle+1]    #copy split list to left and right variables
    R = A[middle+1: last+1]

    L.append(9999999999999999) #add a large num behind for later comparison for L[i] so that it won't go out of range
    R.append(9999999999999999)

    i = j = 0
    print("new stack")
    print("left "+str(L))
    print("right "+str(R))
    for k in range(first, last+1):      
        if L[i] < R[j]:               #if Left side is smaller than, then copy it into A
            A[k] = L[i]
            i+=1

        else:
            A[k] = R[j]   #else, copy the right item up to arr
            j+=1
    print(A)
a = merge_sort([3,2,5,3,7,5,1,4])
print(a)
