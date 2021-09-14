import random

def coinflip(n):
    if n == 0:
        return random.randint(0,1)
    else:
        heads = coinflip(n-1)
        heads += random.randint(0,1)
        return heads


def main():
    n = int(input("enter # of flips: "))
    print(coinflip(n))

main()
