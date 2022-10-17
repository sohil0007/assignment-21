def printN(n):

    if n>0:
        printN(n-1)
        print(n,end=' ')

n = int(input("Enter a number:"))
printN(n)        
