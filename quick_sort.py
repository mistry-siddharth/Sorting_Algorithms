def quickSort(a):
    '''
    this function calls quickSort2 recursively while taking just one input
    which is the list to be sorted.
    '''
    quickSort2(a, 0, len(a)-1)

def quickSort2(a, low, hi):
    '''
    this function recusrsively calls function partion and itself to do
    sorting. It does that only if more than one element is to be sorted
    '''
    if low < hi:
        pindex = partition(a, low, hi)
        quickSort2(a, low, pindex-1)
        quickSort2(a, pindex+1, hi)

def partition(a, low, hi):
    '''
    this is the heart of the algorithm. What this does is takes a pivot value
    and swaps values to its left which are less than its value. Values greater
    than pivot are moved to the right
    '''
    pivot = get_pivot(a, low, hi) #returns index of the pivot value
    pivotvalue = a[pivot] #stores the pivotvalue from pivot index
    a[pivot], a[low] = a[low], a[pivot] #swaps with the left most element in the array
    pindex = low #assigns a counter for swapping if element value < pivot value

    for x in range(low, hi+1): #+1 because the pivot value got moved to the front
        if a[x] < pivotvalue:
            pindex += 1 #increments border value or pivot pointer for swapping
            a[x], a[pindex] = a[pindex], a[x]

    #brings the pivot value in the center. thereby creating left and right sublists        
    a[low], a[pindex] = a[pindex], a[low]
    return pindex
    
def get_pivot(a, low, hi):
    #gets the median value, from first, last and end value
    
    mid = (low + hi)//2
    pivot = hi #by default set to the last element index
    
    if a[low] < a[mid]:
        if a[mid] < a[hi]:
            pivot = mid #selects the element with median value and returns its index
    elif a[low] < a[hi]: #when there are only two elements, it by default selects the low value
        pivot = low
    return pivot

a = [2,4,1,5,8,3,6,9]
quickSort(a)
print(a)
