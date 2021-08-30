n,m = map(int,input().split())

resultArr = []

for i in range(n):
    data = list(map(int, input().split()))
    resultArr.append(min(data))

resultMax = max(resultArr)

print(resultMax, "최대 정답")