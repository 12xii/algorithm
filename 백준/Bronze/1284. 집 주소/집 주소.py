while True:
    n = list(map(int, list(input())))
    if(n[0] == 0): 
        break
    sum = 2
    for i in n:
        if i == 0:
            sum += 4
        elif i == 1:
            sum += 2
        else:
            sum += 3
    sum += len(n) - 1
    print(sum)