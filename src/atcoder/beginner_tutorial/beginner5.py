a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = 500
y = 100
z = 50

cnt = 0
for i in range(0, a+1):
    for j in range(0, b+1):
        for k in range(0, c+1):
            if x * i + y * j + z * k == d:
                cnt = cnt+1


print(cnt)

