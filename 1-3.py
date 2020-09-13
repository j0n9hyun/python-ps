import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
nc = list(map(int, input().split()))

average = round(sum(nc) / n)  # 학생들의 평균
min = 2147000000

for i, x in enumerate(nc):
    tmp = abs(x - average)
    # print(tmp)
    if (tmp < min):
        min = tmp
        score = x
        res = i + 1
    elif (tmp == min):
        if (x > score):
            score = x
            res = i + 1
print(average, res)