x = int(input())
sticks = [64]

while(sum(sticks) > x):
    m = min(sticks)
    sticks.remove(m)
    sticks.append(m / 2)
    if(sum(sticks) < x):
        sticks.append(m / 2)

print(len(sticks))