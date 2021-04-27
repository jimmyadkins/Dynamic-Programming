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

def collatz_rec(num):
    step = 0
    if num == 1:
        return step
    if (num % 2) == 0:
        step = collatz_rec(num/2) + 1
    else:
        step = collatz_rec(num*3+1) + 1
    return step

def collatz_dyn(n):
    # too much work rn don't need to finish



test_num = 21


print()
tic = time.perf_counter()
result = collatz_whi(test_num)
toc = time.perf_counter()
speed = toc-tic
print(f"While Loop: {test_num} --> {result} in {speed}s")

print()
tic = time.perf_counter()
result = collatz_rec(test_num)
toc = time.perf_counter()
speed = toc-tic
print(f"Recursion: {test_num} --> {result} in {speed}s")

print()
tic = time.perf_counter()
result = collatz_dyn(test_num)
toc = time.perf_counter()
speed = toc-tic
print(f"Dynamic Prog: {test_num} --> {result} in {speed}s")