N = int(input())

for i in range(N):
    strArr = ''
    for j in range(N - i - 1):
        strArr += ' '
    for k in range(i + 1):
        strArr += '*'
    print(strArr)