def insertionSort(inplist):

    for i in range(1, len(inplist)):
        for j in range(i-1, -1, -1):
            if inplist[j] > inplist[j+1]:
                inplist[j], inplist[j+1] = inplist[j+1], inplist[j]
            else:
                break
    return inplist

'''
        j = i-1
        while(inplist[j] > inplist[j+1] and j >= 0):
            inplist[j], inplist[j] = inplist[j+1], inplist[j+1]
            j -= 1
        
        
        #shifting method
        for i in range(len(inplist)):
            curNum = inplist[i]
            for j in range(i-1, -1, -1):
                if inplist[j] > curNum:
                    inplist[j+1] = inplist[j]
                else:
                    inplist[j+1] = curNum
                    break
'''

inplist = [7,8,3,5,2,1,6]
print(insertionSort(inplist))
