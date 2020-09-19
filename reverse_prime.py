import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
m = list(map(int, input().split()))
print(n, m)