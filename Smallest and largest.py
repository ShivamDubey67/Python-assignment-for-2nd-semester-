l = [23, 5, 11, 6, 2, 3]

def swap(first, second):

    temp = l[first]

    l[first] = l[second]

    l[second] = temp

for i in range(len(l)):

    for j in range(1, len(l)-i):

        if l[j] < l[j-1]:

            swap(j, j-1)

print(l)
