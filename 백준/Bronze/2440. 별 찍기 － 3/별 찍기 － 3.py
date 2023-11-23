N = int(input())

for i in range(N):
    strArr = ''
    for k in range(N - i):
        strArr += '*'
    print(strArr)