def odd(n):

    if n>0:
        odd(n-1)
        print(2*n-1,end=' ')

n = int(input("Enter a number:"))
odd(n)