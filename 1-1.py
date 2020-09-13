import sys
sys.stdin = open('input.txt', 'rt')
t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1:e]
    print(type(a))
    a.sort()
    print(a)
    # print("#%d %d" % (i + 1, a[k - 1]))
