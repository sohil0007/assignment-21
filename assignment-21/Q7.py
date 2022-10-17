def squares(n):

    if n>0:
        squares(n-1)
        print(n**2,end=' ')

n = int(input("Enter a number:"))
squares(n)