def sumList_iterative(L):
    """ Iterative function to accumulate all items in L and return the sum """
    sum = 0
    for num in L:
        sum += num
    return sum


def sumList_recursive(L):
    """ Recursive function to accumulate all items in L and return the sum """
    if len(L) == 1:
        return L[0]
    else:
        sum = sumList_recursive(L[1:])
        sum += L[0]
        return sum


def count_iterative(x, L):
    """ Iterative function to return how many of x are in L """
    count = 0
    for item in L:
        if item == x:
            count += 1
    return count


def count_recursive(x, L):
    """ Recursive function to return how many of x are in L """
    if len(L) == 1:
        return int(L[0] == x)
    elif L[0] == x:
        return count_recursive(x, L[1:]) + 1
    else:
        return count_recursive(x, L[1:])


def main():
    L = [0,1,2,3]
    print("The sum of all items in list: %s = %d" % (L, sumList_iterative(L)))
    print("The sum of all items in list: %s = %d" % (L, sumList_recursive(L)))

    L = [1,2,8,2,2]
    x = 2
    print("%d appears in the list: %s %d times" % (x, L, count_iterative(x, L)))
    print("%d appears in the list: %s %d times" % (x, L, count_recursive(x, L)))


main()
