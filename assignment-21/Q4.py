def odd(n):

    if n>0:
        print(2*n-1,end=' ')
        odd(n-1)

n = int(input("Enter a number:"))
odd(n)