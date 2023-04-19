import sys
def sol():
    n, *target = map(int, sys.stdin.buffer.read().splitlines())
    target=sorted(target)
    for i in target:
        print(i)
sol()