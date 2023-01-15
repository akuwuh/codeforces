test = input()
for i in range(int(test)):

    line1 = input()
    line2 = input()

    x = line1.split()
    y = line2.split()
    n1 = int(x[0]) #8 
    n2 = int(x[-1]) #10
    n3 = int(y[0]) #3
    n4 = int(y[-1]) #4

    if ((n1 < n2 and n3 < n4) or (n1 > n2 and n3 > n4)) and ((n1 > n3 and n2 > n4) or (n1 < n3 and n2 < n4)):
        print("YES")
    else:
        print("NO")