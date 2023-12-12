cases = int(input())

for i in range(cases):
    repeat, word = input().split(' ')
    repeat = int(repeat)
    word = list(word)

    arr = []
    
    for j in word:
        for k in range(repeat):
            arr += j
    print(''.join(arr))