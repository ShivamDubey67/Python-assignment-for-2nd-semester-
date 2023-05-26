def sumofsq(n):

    if n == 1:

        return n

    return n*n + sumofsq(n-1)

print(sumofsq(10))
