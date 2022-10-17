def multi(n,times):

    if times>0:
        multi(n,times-1)
        print(n*times)

n=int(input("Enter a number:"))
times=int(input("times:"))
multi(n,times)        