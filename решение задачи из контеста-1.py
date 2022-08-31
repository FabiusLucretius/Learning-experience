n, k = map(int, input().split())
a = [int(input()) for i in range (n)]
a = sorted(a)
count = 0
p = n // k + 1
for i in range (p):
    for j in range (a):
        res = p[i] * a[j]
        count += res
        print(count)