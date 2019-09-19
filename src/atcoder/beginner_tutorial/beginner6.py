N, A, B = map(int, input().split())

result = 0
for i in range(A, N+1):
    calc = sum([int(v) for v in list(str(i))])
    if A <= calc & calc <= B:
        result += i

print(result)