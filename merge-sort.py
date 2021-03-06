from random import shuffle

"""                       INSTRUCTIONS
        When you get this up and running, copy-paste your merge() and
        mergeSort() functions into your sorts.py file.
        This way, all of your sorting algorithms will be in one place.    """

def merge(leftL, rightL, L):
    """ Implement the merge() function below and you should be good to go """
    NEED_SORT = True
    while NEED_SORT:
        if leftL[0] <= rightL[0]:
            L.append(leftL)
        else:
            L.append(rightL)


def mergeSort(L):
    if len(L) > 1:
        half = len(L) // 2		 # split into two lists
        L1 = L[0:half]
        L2 = L[half:]
        mergeSort(L1)			 # sort each list
        mergeSort(L2)
        merge(L1,L2,L)		     # merge them back into one sorted list


def main():
    N = 10
    L = []
    LCopy = []
    for i in range(10):
        L.append(i)
        LCopy.append(i)

    shuffle(L)
    print(L)
    mergeSort(L)
    assert L == LCopy
    print(L)

main()
