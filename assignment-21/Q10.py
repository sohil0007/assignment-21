def rev(n):

    if n//10==0:
        print(n)
        return n
    print(n%10,end='')
    rev(n//10)

n=int(input("Enter a number:"))
rev(n)        