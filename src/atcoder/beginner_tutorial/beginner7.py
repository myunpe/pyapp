num = int(input())
values = [int(v) for v in input().split()]
values.sort(reverse=True)
a_total = 0
b_total = 0


for index in range(0, len(values)):
    if index % 2 == 0:
        a_total += values[index]
    else:
        b_total += values[index]

print(a_total - b_total)