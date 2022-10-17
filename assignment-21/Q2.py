def printN(n):

    if n>0:
        print(n,end=' ')
        printN(n-1)

n = int(input("Enter a number:"))
printN(n)   