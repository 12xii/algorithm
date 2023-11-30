count, cases = int(input()), list(map(int, input().split()))
y, m = 0, 0

for i in range(count):
    y += cases[i] // 30 + 1
    m += cases[i] // 60 + 1

y *= 10
m *= 15

if(y < m):
    print(f"Y {y}")
elif (m < y):
    print(f"M {m}")
else:
    print(f"Y M {y}")