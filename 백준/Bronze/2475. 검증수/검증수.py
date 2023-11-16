l = list(map(int, input().split()))
sum = 0

for x in l:
    sum += x ** 2

print(sum % 10)