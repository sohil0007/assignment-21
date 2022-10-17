def cubes(n):

    if n>0:
        cubes(n-1)
        print(n**3,end=' ')

n = int(input("Enter a number:"))
cubes(n)