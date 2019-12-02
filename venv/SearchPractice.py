# Used as linear search i.e. one by one comparison search
"""list = [5, 8, 4, 6, 9, 2]
n = 11
pos = 0
def search(list, n):
    for x in list:
        if x == n:
            i = list.index(x) + 1
            globals()['pos'] = i
            return  True

    return False
if search(list, n):
    print("found "+str(n)+" in the list at position "+str(pos)+".")
else:
    print("Not present in the list")
# used for binary search: binary search is whole mechanism and faster than linear search, for binary search list should be sorted.
list = [4, 7, 8, 12, 45, 99]
upperIndex = len(list) - 1
lowerIndex = 0
n = 45
pos = 0

def middleIndex(li, ui):

    mi = (li + ui) // 2
    return mi

def search (list, n):

    for x in list:
        mi = middleIndex(globals()['lowerIndex'],globals()['upperIndex'])
        if x == n:
            globals()['pos'] = list.index(x) + 1
            return True
        elif list[mi] > n:
            globals()['upperIndex'] = mi
        else:
            globals()['lowerIndex'] = mi

if search(list, n):
    print("found "+str(n)+" in the list at position "+str(pos)+".")
else:
    print("not found")

# Bubble sort: it will swap the elements and compare them in ascending order.
list = [5, 3, 8, 6, 7, 2]
def sort(list):
    for x in range(len(list)-1,0,-1):
        for y in range(x):
            if list[y] > list[y + 1]:
                temp = list[y]
                list[y] = list[y + 1]
                list[y+ 1] = temp

sort(list)

print(list)"""


#selection sort:
list = [5, 3, 8, 6, 7, 2]
def sort(list):
    for x in range(5):
        minpos = x
        for y in range(x,6):
            if list[y] < list[minpos]:
                minpos = y

        temp = list[x]
        list[x] = list[minpos]
        list[minpos] = temp

sort(list)

print(list)