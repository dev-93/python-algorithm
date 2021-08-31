def recursive_funciton(i):
    if i == 100:
        return
    print(i, '번쨰 재귀 함수에서', i + 1, '번째 재귀 함수 호출')
    recursive_funciton(i + 1)
    print(i,'번쨰 재귀 함수 종료')


recursive_funciton(1)

def factorial_func(i):
    if i <= 1:
        return 1
    return i * factorial_func(i - 1)


print(factorial_func(5))
