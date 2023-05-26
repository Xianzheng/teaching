lst = [1,2,4,3,1]

def swap(thlst, p1, p2):
    temp = thlst[p1]
    thlst[p1] = thlst[p2]
    thlst[p2] = temp
    return thlst

def bubblesort(alst,end,id):
    swapped = 0
    if id == end:
        return alst
    for i in range(0,end-1):
        if alst[i] < alst[i+1]:
            swap(alst, i, i+1)
            swapped = 1
    if swapped == 1:
        alst = bubblesort(alst,end-id,id+1)
    return alst

print(bubblesort(lst,len(lst),0))