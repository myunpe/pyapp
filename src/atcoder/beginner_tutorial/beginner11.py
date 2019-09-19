total = int(input())


b_num = 0
b_x = 0
b_y = 0
for i in range(total):
    num, x, y = map(int, input().split())
    mn = num - b_num
    mx = abs(x - b_x)
    my = abs(y - b_y)

    if mn < mx + my:
        print("No")
        exit()
    else:
        if b_num % 2 == (mx + my) % 2:
            mn = num
            b_x = x
            b_y = y
        else:
            # print("{} {} {}".format(b_num, mx, my))
            print("No")
            exit()

print("Yes")
    