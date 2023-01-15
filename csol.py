i = int(input())
 
for j in range(i):
    k, n = map(int, input().split())
    h = 1
    print(str(1) + " ")
    for l in range(1, k):
        if (n - h - l + 1) >= k - l:
            h += l
        else:
            h = h + 1
        print(str(h) + " ")
    print("")
        