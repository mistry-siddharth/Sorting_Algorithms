def selectionSort(inplist):
    
    for i in range(len(inplist)-1):
        min_num = i
        for j in range(i + 1, len(inplist)):
            if inplist[j] < inplist[min_num]:
                print('min num before', min_num)
                min_num = j
                print('min num after', min_num)
        if min_num != i:
            inplist[i], inplist[min_num] = inplist[min_num], inplist[i]
    return inplist

inplist = [2,7,9,8,5,6]
print(selectionSort(inplist))
