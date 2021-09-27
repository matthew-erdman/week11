def maxOfList(L):

    if len(L) == 2:
        return L[1] if L[1] > L[0] else L[0]

    else:
        return maxOfList(L[1:]) if maxOfList(L[1:]) > L[0] else L[0]

def maxOfListExpanded(L):
    if len(L) == 2:
        if L[1] > L[0]:
            return L[1]
        else:
            return L[0]

    else:
        if maxOfList(L[1:]) > L[0]:
            return maxOfList(L[1:])
        else:
            return L[0]


# def isSorted(L):
#     pass

def fibonacci(n):

    if n == 1:
        print(1)
        return 1

    else:
        sum = fibonacci(n-1) + fibonacci(n)
        print(sum)
        return sum

# def bernoulli(n):
#     pass



def main():
    L = [15, 8, 3, 19, 9, 5, 11]
    print("maxOfList: %s" % maxOfList(L))

    n = 5
    print("fibonacci: %s" % fibonacci(n))



main()
