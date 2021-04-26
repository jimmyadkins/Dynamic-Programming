import time

def collatz_whi(num):
    result = 0
    while num!=1:
        if (num % 2) == 0:
            num = num/2
            result = result + 1
        else:
            num = num*3 + 1
            result = result + 1
    return result

def collatz_rec(num, steps):
    print(steps)
    if (num % 2) == 0:
        num = num / 2
        steps = steps + 1
        collatz_rec(num, steps)
    elif num != 1:
        num = num * 3 + 1
        steps = steps + 1
        collatz_rec(num, steps)
    else:
        print(steps)
        return steps

def collatz_dyn(num, arr):
    result = 0
    while num!=1:
        if (num % 2) == 0:
            num = num/2
            result = result + 1
        else:
            num = num*3 + 1
            result = result + 1
    return result

test_num = 3


print()
tic = time.perf_counter()
result = collatz_whi(test_num)
toc = time.perf_counter()
speed = toc-tic
print(f"While Loop: {test_num} --> {result} in {speed}s")

print()
tic = time.perf_counter()
result = collatz_rec(test_num, 0)
print(result)
toc = time.perf_counter()
speed = toc-tic
print(f"Recursion: {test_num} --> {result} in {speed}s")

print()
tic = time.perf_counter()
result = collatz_dyn(test_num)
toc = time.perf_counter()
speed = toc-tic
print(f"Dynamic Prog: {test_num} --> {result} in {speed}s")