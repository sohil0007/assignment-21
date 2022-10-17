def even(n):

    if n>0:
        print(2*n,end=' ')
        even(n-1)

n = int(input("Enter a number:"))
even(n)