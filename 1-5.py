import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
nc = list(map(int, input().split()))
# print(nc)


def digits_sum(x):
    sum = 0
    while (x > 0):
        sum += x % 10
        x /= 10
    return sum


for x in nc:
    digits_sum(x)

print(x)