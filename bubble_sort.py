'''
bubblesort: Its a relatively simple and slow algorithm.
Works fine for small number of arguments. But becomes
slow when it comes to sorting saw millions of items

here j goes from len-1-i, because in as the swapping starts,
the largest element will be sorted and will be already at the
end. So you dont need to go back to the last element and do
the check to sort
'''

def bubbleSort(inplist):
    for i in range(len(inplist)-1):
        for j in range(len(inplist)-1-i):
            if inplist[j] > inplist[j+1]:
                inplist[j], inplist[j+1] = inplist[j+1], inplist[j]
    return inplist

inplist = [1,4,5,2,6,3,9,7,8]
print(bubbleSort(inplist))
