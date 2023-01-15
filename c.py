test = input()

for i in range(int(test)):
    seen = set()
    line = input()

    x = line.split()

    k = int(x[0])
    n = int(x[-1])

    ans = [1]
    curr = 1
    inc = 0 

    mmm = False
    add = False
    subtract = False
    
    if k == n:
        for i in range(k):
            print(i + 1, end='') 
            print(" ", end='')

    else:
        for i in range(k - 1): #0 -> k-2 therefore accesses index before

            inc +=1
            curr = ans[i] + inc

            if(add == True):
                ans.append(ans[i] + 1)
                continue
            if(subtract == True):
                ans.append(ans[i] - 1)
                continue

            if curr >= n :
                mmm = True
                if curr == n:
                    ans.append(curr)
                    continue

            if mmm == True: #if max has been reached 
                if ((n- ans[i]) >= (k - 1) - i):
                    add = True
                    ans.append(ans[i] + 1)
                else:
                    subtract = True
                    ans.append(ans[i] -1)
                continue
    

            ans.append(curr)

        ans.sort()

        for i in range(len(ans)):
            if i == len(ans) - 1: #last one
                print(ans[i])
                break
            print(ans[i], end='')
            print(" ", end='')






