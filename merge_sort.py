def mergeSort(a):
    n = len(a)
    if n < 2:
        return a
    else:
        mid = n//2
        left = a[:mid]
        right = a[mid:]
        
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
            
        while (i < len(left)):
            a[k] = left[i]
            i += 1
            k += 1
        while (j < len(right)):
            a[k] = right[j]
            j += 1
            k += 1
    return a

a = ['b','g','r','t','x','d','a','z']
print(mergeSort(a))
