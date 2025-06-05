def rotLeft(a, d):
    copy = a[:]
    j = 0
    for i in range(len(a)):
        if i+d <= len(a)-1:
            a[i] = copy[i+d]
        else:
            a[i] = copy[j] 
            j+=1

    return a

d = 4
a = [1, 2, 3, 4, 5]

rotLeft(a,d)