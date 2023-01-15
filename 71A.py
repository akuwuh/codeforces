n = input()
for i in range(int(n)):
    word = input()
    length = len(word)
    if length > 10:
        ans = word[0] + str(length - 2) + word[-1]
        print(ans)
    else:
        print(word)

