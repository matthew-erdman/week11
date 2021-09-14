def binarySearch(x, ls):
    """
    Purpose: A recursive implementation of binary search.
    Parameters: x - the value to search for
             ls - a list of values to search through (ls should be sorted)
    Return: True if x is in ls
    """
    if len(ls) == 0: #base case 1 - no values to search
        return False

    mid = len(ls)//2
    if ls[mid] == x: #base case 2 - found the value x
        return True

    if x < ls[mid]: #recursive case 1 - x is in left half
        return binarySearch(x,ls[0:mid]) #left half of ls (0 to mid-1)
    else:
        return binarySearch(x,ls[mid+1:]) #right half of ls (mid+1 to end)

def main():
    L = [0,1,2,3,4,5,6,7,8,9]

    num = 4
    if binarySearch(num, L) == True:
        print("item: %2d   found in      L %s" % (num, L))
    else:
        print("item: %2d   NOT found in  L %s" % (num, L))

    num = 24
    if binarySearch(num, L) == True:
        print("item: %2d   found in      L %s" % (num, L))
    else:
        print("item: %2d   NOT found in  L %s" % (num, L))


main()
