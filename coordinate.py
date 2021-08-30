n = int, input()

num = int(n[1])

x = 1
y = 1

plans = input().split()

for plan in plans:
    if plan == "R":
        y += 1
    elif plan == "L":
        y -= 1
    elif plan == "U":
        x -= 1
    elif plan == "D":
        x += 1

    if (x < 1):
        x += 1
        continue
    elif (x > num):
        x -= 1
        continue
    elif (y < 1):
        y += 1
        continue
    elif (y > num):
        y -= 1
        continue

print(x, y)
