import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
r = 0

while n >= k:
    while n % k != 0:
        n -= 1
        r += 1
    n //= k
    r += 1
while n > 1:
    n -= 1
    r += 1
print(r)
