def minimumBribes(q):
    Bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                Bribes += 1
    print(Bribes)

q = [2, 1, 5, 3, 4]
minimumBribes(q)