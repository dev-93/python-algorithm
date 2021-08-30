n, k = map(int, input().split())

result = 0

while n >= k:
    if ( n % k == 0):
        n = n // k
        result += 1
    else:
        n = n-1
        result += 1

    print(n)
print(result, "결과")
