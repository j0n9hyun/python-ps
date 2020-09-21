import sys
sys.stdin = open('input.txt', 'r')
n, m, k = map(int, input().split())  # 5 8 3
data = list(map(int, input().split()))  # 2 4 5 4 6
data.sort()  # 2 4 4 5 6
fir = data[n - 1]  # 6
sec = data[n - 2]  # 5
r = 0

while True:
    for i in range(k):
        if m == 0:
            break
        r += fir
        m -= 1  # whenever add, subtract 1
    if m == 0:
        break
    r += sec
    m -= 1

print(r)

# mathematical approach

# cnt = int(m / (k + 1)) * k
# cnt += m % (k + 1)
# r += cnt * fir
# r += (m - cnt) * sec
# print(r)
