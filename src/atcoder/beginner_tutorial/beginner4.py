n = input()
data = [int(v) for v in input().split()]
isEven = all([d % 2 == 0 for d in data])
cnt = 0
while isEven:
    data = [d / 2 for d in data]
    isEven = all([d % 2 == 0 for d in data])
    cnt = cnt+1

print(cnt)